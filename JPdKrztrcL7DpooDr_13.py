
def collatz(n):
  maximum = n
  steps = 0
  while n != 1:
    if n>maximum:
      maximum = n
    if n%2==0:
      n = n/2
    else:
      n = n*3+1
    steps += 1
  return [steps, maximum]

