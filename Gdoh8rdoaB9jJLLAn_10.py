
def summation(exp, num):
  to_add = []
  for n in range(1, num + 1):
    to_add.append(eval(exp))
  return round(sum(to_add),1)

