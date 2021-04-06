
def simple_check(a, b):
  c = 0
  n = sorted([a,b])
  while n[0] > 0:
    if not n[1] % n[0]:c+=1
    n = [x-1 for x in n]
  return c

