
def iqr(lst):
  lst.sort()
  if len(lst)%2==1:
    q1=lst[:int((len(lst)-1)/2)]
    q3=lst[int((len(lst)+1)/2):]
  else:
    q1=lst[:int(len(lst)/2)]
    q3=lst[int(len(lst)/2):]
  return(quartile(q3)-quartile(q1))
  
def quartile(q):
  if len(q)%2==1:
    return (q[int((len(q)-1)/2)])
  else:
    return((q[int(len(q)/2-1)]+q[int(len(q)/2)])/2)

