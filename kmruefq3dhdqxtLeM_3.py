
def sum_digits(a, b):
  return sum([ sum([ int(i) for i in str(ele)]) for ele in range(a, b + 1, 1)])

