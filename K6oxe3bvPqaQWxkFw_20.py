
def join_digits(n): #w/o built-in
  start, lst = 0, []
  while start < n:
    start += 1
    lst += [start]
  s, t, new, i = [x for x in lst if x < 10], [x for x in lst if x >= 10], [], []
  for x in t:
    while x > 0:
      i += [x % 10]
      x //= 10
    new += [i]
    i = []
  u = [x for y in [x[::-1] for x in new] for x in y]
  v = s + u
  d = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}
  to_str = [d[x] for x in v]
  st = ""
  for x in to_str:
    st += x + '-'
  return st[:-1]
​
def join_digits(n):
  return '-'.join(x for y in [str(i) for i in range(1, n + 1)] for x in y)

