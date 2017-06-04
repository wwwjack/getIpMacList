import glob
import os


def getlist(num):
    ipmaclist = {}
    ip = ""
    f = open(glob.glob("oriInfo/info-"+str(num+1)+"-*.txt")[0])
    for line in f:
        if line.__len__() > 23:
            if line[21] == "1":
                ip = line[21:23]+line[24:27]+line[28:29]+"0"*(3-line[30:-1].__len__())+line[30:-1]
        if line.__len__() > 15:
            if line[15] == ":":
                ipmaclist[ip] = line[13:30]
    f.close()
    return ipmaclist


def output(mdir):
    llist = sorted(mdir.iteritems(), key=lambda d: int(d[0]), reverse=False)
    ipf = open("ip.txt", "w")
    ipmacf = open("ip-mac.txt", "w")
    for i in range(llist.__len__()):
        ipOld = llist[i][0]
        if ipOld[6] == "0":
            if ipOld[7] == "0":
                ip = ipOld[0:2] + "." + ipOld[2:5] + "." + ipOld[5:6] + "." + ipOld[8:] + "\n"
            else:
                ip = ipOld[0:2] + "." + ipOld[2:5] + "." + ipOld[5:6] + "." + ipOld[7:] + "\n"
        else:
            ip = ipOld[0:2] + "." + ipOld[2:5] + "." + ipOld[5:6] + "." + ipOld[6:] + "\n"
        ipf.write(ip)
        ipmacf.write(ip[:-1] + " "*(13 - str(ip).__len__()) + "   ----->" + "   " + llist[i][1] + "\n")
    ipf.close()
    ipmacf.close()


def upcache(mdir):
    ipmacf = open("cache/ip-mac-cache.txt", "w")
    ipf = open("cache/ip-cache.txt", "w")
    for key in mdir:
        ipf.write(key+"\n")
        ipmacf.write(key+"   ------>   "+mdir[key]+"\n")
    ipmacf.close()
    ipf.close()


def readcache():
    mdir={}
    ipmacf = open("cache/ip-mac-cache.txt", "r")
    ipf = open("cache/ip-cache.txt", "r")
    for linekey in ipf:
        for linevalue in ipmacf:
            if linevalue[0:linekey.__len__()-1] == linekey[:-1]:
                mdir[linekey[:-1]] = linevalue[22:-1]
                break
    ipmacf.close()
    ipf.close()
    return mdir



def main():
    mdir=readcache()
    fnum = os.listdir("oriInfo").__len__()
    for i in range(fnum):
        mdir.update(getlist(i))
    upcache(mdir)
    output(mdir)

if __name__ == main():
    main()
