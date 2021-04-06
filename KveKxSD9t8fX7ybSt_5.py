
def final_countdown(l):
  s=[]
  while l:
    if 1 in l:
      r,p=[1],l.index(1)
      if p==0:l=l[1:]
      else:
        if l[p-1]==2:
          i=p-1
          while True:
            r[:0]=[l[i]]
            if i>0 and l[i-1]==l[i]+1:i-=1
            else:break
          del l[i:p+1]
        else:l=l[p+1:]
      s.append(r)
    else:break
  return[len(s),s]

