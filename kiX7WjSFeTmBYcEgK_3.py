
def major_sum(lst):
  P=sum([x for x in lst if x>0])
  N=abs(sum([x for x in lst if x<0]))
  Z=lst.count(0)
  if max(P,N,Z)==P:
    return P
  elif max(P,N,Z)==N:
    return (-1)*N
  else:
    return Z

