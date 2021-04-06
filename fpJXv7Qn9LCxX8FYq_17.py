
def solve(eq):
  x = eq.split(' ')
  if x[1] == '+':
    result = int(x[4]) - int(x[2])
    return result
  elif x[1] == '-':
    result = int(x[4]) + int(x[2])
    return result

