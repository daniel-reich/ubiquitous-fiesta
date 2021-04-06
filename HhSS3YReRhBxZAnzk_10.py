
def gen_values(n, i):
  lst = []
  x = 0
  while round(x, 2) <= n:
    lst.append(round(x, 2))
    x += i
  return lst

