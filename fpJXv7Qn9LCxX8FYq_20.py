
def solve(eq):
  lst = eq.replace(' ','').replace('x','').replace('+','').split('=')
  return int(lst[1])-int(lst[0])

