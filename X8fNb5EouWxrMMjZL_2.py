
def collatz(num):
  steps = 0
  while num != 1:
    num = (3 * num + 1) if num%2 else (num // 2)
    steps += 1
  return steps

