
def square_root(n):
  m=int(str(n)[::2])
  while m*m!=n: m+=(n//m-m)//2
  return m

