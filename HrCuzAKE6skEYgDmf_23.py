
def pairs(lst):
  return [[lst[x], lst[-x-1]] for x in range(int(len(lst)/2+0.6))] if lst else []

