
def pairs(lst):
  return [[lst[i], lst[-i-1]] for i in range(int(len(lst)/2+0.5))]

