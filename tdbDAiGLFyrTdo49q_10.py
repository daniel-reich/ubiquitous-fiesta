
def find_difference(a, b):
  from numpy import prod
  return abs(sum(map(prod, [a, [i*-1 for i in b]])))

