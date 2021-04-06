
def collatz(n):
  count = 0
  max = n
  while(n != 1):
    if(n % 2 == 0):
      n /= 2
    else:
      n = (n * 3) + 1
      
    if(max < n):
      max = n
      
    count += 1
      
  return [count, max]

