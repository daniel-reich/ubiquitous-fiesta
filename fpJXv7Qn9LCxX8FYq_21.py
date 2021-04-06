
def solve(eq):
  split = eq.split(' ')
  if split[1] == '+':
    return int(split[4]) - int(split[2])
  elif split[1] == '-':
    return int(split[4]) + int(split[2])

