
def pairs(lst):
  x = int(len(lst)/2+.5)
  return list(map(list, zip(lst[:x], lst[::-1][:x])))

