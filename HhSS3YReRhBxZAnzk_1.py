
def gen_values(n, i):
  a = []
  b = 0.0
  while not b>n:
    a.append(b)
    b = round(b+i,2)
  return a

