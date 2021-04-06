
def amount_fib(n):
  a = 0
  b = 1
  flist = [0,1]
  while a+b < n:
    flist.append(a+b)
    c=a
    a=b
    b=c+a
  ctr = 0
  for i in range(len(flist)):
    if flist[i] < n:
      ctr += 1
  return ctr

