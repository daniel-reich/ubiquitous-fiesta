
def happy(n):
  def f(n):
    return sum(int(d)**2 for d in str(n))
  l=[]
  while True:
    n=f(n)
    if n==1:
      return True
    if n in l:
      return False
    l = l + [n]

