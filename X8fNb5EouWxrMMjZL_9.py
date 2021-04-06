
def collatz(num):
  num_steps = 0
  while num != 1:
    if num % 2 == 0:
      num = num / 2
      num_steps += 1
      continue
    if num % 2 != 0:
      num = num * 3 + 1
      num_steps += 1
      continue
  return num_steps

