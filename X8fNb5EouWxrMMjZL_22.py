
def collatz(num):
  steps = 0
  c = num
  while c != 1:
    if c % 2 == 0:
      c = c // 2
    else:
      c = c * 3 + 1
    steps += 1
  return steps

