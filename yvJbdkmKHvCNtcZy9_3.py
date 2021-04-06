
def is_disarium(n):
  s = 0
  a = str(n)
  bb = [int(a[x]) for x in range(len(a))]
  for x in range(len(bb)):
    s += bb[x] **(x + 1)
  return s == n

