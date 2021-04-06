
def solve(eq):
  lst = eq.split(' ')
  if lst[1] == '+':
    return eval(lst[-1] + '-' + lst[2])
  elif lst[1] == '-':
    return eval(lst[-1] + '+' + lst[2])

