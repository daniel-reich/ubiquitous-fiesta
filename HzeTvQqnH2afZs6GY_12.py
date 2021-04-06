
def generate_rug(n, direction):
  dict = {"left": 1, "right": 0}
  lst, x = [], 0
  d = dict.get(direction)
  l = (1 if d else 0)
  r = (0 if d else 1)
  for i in range(0, n):
    f = x*l + (n-x-1)*r
    s = (x+1)*r + (n-x)*l
    lst.append([i for i in range(f, 0, -1)] + [i for i in range(0, s)])
    x += 1
  return lst

