
def collatz(n):
​
  i,m = 0,1
​
  while n!=1:
  
    if n%2:
      n = n*3+1
    else:
      n /= 2
​
    m = int(m if m>n else n)
    i += 1
​
  return [i,m]

