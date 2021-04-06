
def collatz(n):
  cnt=0
  mx=n
  while n!=1:
    if n%2:
      n=n*3+1
    else:
      n=n/2
    cnt+=1
    mx=max(mx,n)
  return [cnt, mx]

