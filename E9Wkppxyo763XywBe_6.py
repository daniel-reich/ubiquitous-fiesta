
def binary_clock(time):
    time=time.split(':')
    hh=list(time[0])
    mm=list(time[1])
    ss=list(time[-1])
    row=[]
​
    c1='0000'+bin(int(hh[0]))[2:]
    c2='0000'+bin(int(hh[1]))[2:]
    c3='0000'+bin(int(mm[0]))[2:]
    c4='0000'+bin(int(mm[1]))[2:]
    c5='0000'+bin(int(ss[0]))[2:]
    c6='0000'+bin(int(ss[1]))[2:]
​
​
    print(c1,c2,c3,c4,c5,c6)
    a=" "+c2[-4]+" "+c4[-4]+" "+c6[-4]
    b=" "+c2[-3]+c3[-3]+c4[-3]+c5[-3]+c6[-3]
    c=c1[-2]+c2[-2]+c3[-2]+c4[-2]+c5[-2]+c6[-2]
    d=c1[-1]+c2[-1]+c3[-1]+c4[-1]+c5[-1]+c6[-1]
    row.append(a)
    row.append(b)
    row.append(c)
    row.append(d)
    return row

