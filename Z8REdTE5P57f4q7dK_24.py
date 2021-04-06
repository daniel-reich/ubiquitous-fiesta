
def collatz(n):
  max_number = 0
  steps = 1
  while n != 1:
    if n % 2 == 0:
      n = n // 2
      steps += 1
      if n > max_number:
        max_number = n
    elif n % 2 != 0:
      n = (n*3) + 1
      steps += 1
      if n > max_number:
        max_number = n
  return (steps,max_number)

