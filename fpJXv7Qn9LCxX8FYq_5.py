
def solve(eq):
  lst = eq.split()
  if lst[1] == '+':
    return eval(lst[4] + '-' +lst[2])
  else:
    return eval(lst[4] + '+' +lst[2])

