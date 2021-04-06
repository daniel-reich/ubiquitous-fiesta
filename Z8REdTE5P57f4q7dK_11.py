
def collatz(n):
  l = []
  while n!=1:
    if n%2==0:
      l.append(int(n))
      n /=2
    else:
      l.append(int(n))
      n= 3*n+1
  l.append(1)
  l.sort()
  return (len(l),l[-1])

