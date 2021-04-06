
def break_point(num):
  num=[int(x) for x in str(num)]
  for x in range(len(num)):
    if sum(num[:x])==sum(num[x:]): return True
  return False

