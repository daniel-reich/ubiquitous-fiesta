
def days_between_dates(d1, d2):
    d1s =[d1[4:],d1[2:4],d1[:2]]
    d2s =[d2[4:],d2[2:4],d2[:2]]
    d1s = [int(n) for n in d1s]
    d2s = [int(n) for n in d2s]
    if d1s>d2s: d1s,d2s=d2s,d1s
​
    def incr(date):
        y,m,d = date
        if d<dic[m]: return [y,m,d+1]
        if m==2 and d==28 and sum(y%i==0 for i in [4,100,400])%2: return [y,2,29]
        if m!=12 and d>=dic[m]: return [y,m+1,1]
        return [y+1,1,1]
​
    cnt=0
    while d1s!=d2s:
        d1s = incr(d1s)
        cnt+=1
    return cnt
​
dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

