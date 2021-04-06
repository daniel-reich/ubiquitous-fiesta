
def summation(exp, n):
  exp = exp.replace('n', '{0}')
  return round(sum(eval(exp.format(i)) for i in range(1, n+1)), 1)

