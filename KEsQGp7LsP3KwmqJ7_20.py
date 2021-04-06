
def check(lst):
  x = sorted([x for x in lst])
  for i in range(len(x) - 1):
    x = [x[-1]] + x[:-1] 
    if x == lst: return "YES"
  return "NO"

