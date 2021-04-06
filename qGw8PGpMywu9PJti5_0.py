
def hanoi(n):
  l=[]
  def f(n,s,d,a):
    if n==1:l.append((s,d));return
    f(n-1,s,a,d)
    l.append((s,d))
    f(n-1,a,d,s)
  if n>0:f(n,1,3,2)
  return l

