
def collatz(n):
  step = 1
  high = 0
  while n != 1:
    if n % 2 == 0:
      n *= 0.5
      step += 1
    elif n % 2 != 0:
      n = n * 3 + 1
      step += 1
      if n > high:
        high = int(n)
    
  return (step, high)

