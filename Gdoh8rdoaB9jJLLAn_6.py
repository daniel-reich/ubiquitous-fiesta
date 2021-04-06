
def summation(x, s):
  y = [eval(x.replace('n', str(i))) for i in range(1, s + 1)]
  return round(sum(y), 1)

