
def collatz(n):
  col = [n]
  while n!=1:
    if n%2==0:
      n=n//2
    else:
      n=n*3+1
    col.append(n)
  return [len(col)-1,max(col)]

