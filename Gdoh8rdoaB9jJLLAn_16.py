
def summation(exp, i):
  total = 0
  for num in range(1, i+1):
    total += eval(exp.replace("n", str(num)))
  return round(total, 1)

