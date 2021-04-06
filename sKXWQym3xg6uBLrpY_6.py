
def iqr(lst):
  lst.sort()
  if len(lst)%2==0:
    z=int(len(lst)/2)
    p=lst[:z]
    t=lst[z:]
    if (len(lst)/2)%2==0:
      q=int((len(p)/2))
      i=(p[q]+p[q-1])/2
      y=int((len(t)/2))
      n=(t[y]+t[y-1])/2
      return abs(n-i)
    else:
      q=int((len(p)/2))
      i=p[q]
      y=int((len(t)/2))
      n=t[y]
      return abs(n-i)
  else:
    z=int((len(lst)-1)/2)
    p=lst[:z]
    t=lst[z+1:]
    if ((len(lst)-1)/2)%2==0:
      q=int((len(p)/2))
      i=(p[q]+p[q-1])/2
      y=int((len(t)/2))
      n=(t[y]+t[y-1])/2
      return abs(n-i)
    else:
      q=int((len(p)/2))
      i=p[q]
      y=int((len(t)/2))
      n=t[y]
      return abs(n-i)

