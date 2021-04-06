
def josephus(people):
  import math
  log = math.log(people, 2)
  l = int(log)
  k = people-(2**l)
  return 2*k + 1

