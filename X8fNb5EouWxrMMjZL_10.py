
def collatz(num):
  steps = 0
  while num != 1:
    if num % 2 == 0:
      num = num / 2
    else:
      num = num * 3 + 1
    steps += 1
  return steps

