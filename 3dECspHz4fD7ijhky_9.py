
def numbers_range(lst):
  if lst:
    s=str(lst[0])
    for i in range(1,len(lst)):
      if lst[i-1]+1==lst[i]:
        s+='#'+str(lst[i])
      else:
        s+=' '+str(lst[i])
    A=[x.split('#') for x in s.split()]
    res=''
    for x in A:
      if len(x)<3:
        res+=', '+', '.join(x)
      else:
        res+=', '+x[0]+'-'+x[-1]
    return res[2:]
  else:
    return ''

