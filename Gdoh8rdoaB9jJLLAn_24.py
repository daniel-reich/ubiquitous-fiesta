
def summation(exp, i):
  return round(sum(eval(exp.replace('n', str(n))) for n in range(1, i+1)), 1)

