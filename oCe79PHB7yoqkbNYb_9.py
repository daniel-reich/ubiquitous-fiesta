
def break_point(num):
  x = str(num)
  for i in range(len(x)-1):
    if sum(map(int, x[:i+1])) == sum(map(int, x[i+1:])):
      return True
  return False

