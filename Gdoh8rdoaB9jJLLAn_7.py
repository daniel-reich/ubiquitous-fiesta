
def summation(exp, n):
  the_sum = list(eval(exp.replace('n', str(i))) for i in range(1, n + 1))
  return round(sum(the_sum), 1)

