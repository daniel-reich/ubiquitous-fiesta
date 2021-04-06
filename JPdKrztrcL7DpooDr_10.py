
def collatz(n):
  num_steps = 0
  highest_number = n
  while n > 1:
    n = n / 2 if n % 2 == 0 else n*3 + 1
    highest_number = n if n > highest_number else highest_number
    num_steps += 1
  return [num_steps, highest_number]

