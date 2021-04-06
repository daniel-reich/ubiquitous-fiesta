
import re
def c_cipher(m,k):
  if m.islower():
    x=mi=0
    ml,ms=len(m),list(m)
    col=len(k)
    row=ml//col
    l,d=sorted(list(k)),[]
    for _ in range(row):d+=[[None]*col]
    for _ in range(col):
        i=k.index(l[x])
        for j in range(row):
            d[j][i]=ms[mi]
            mi+=1
        x+=1
    return''.join(''.join(x)for x in d)
  else:
    m=re.sub('[. ]','',m).lower()
    l=len(k)
    t=[m[i:i+l]for i in range(0,len(m),l)]
    if len(t[-1])<l:t[-1]+='x'*(l-len(t[-1]))
    return''.join(y[[sorted(k).index(x)+1for x in k].index(i)]for i in range(1,l+1)for y in t)

