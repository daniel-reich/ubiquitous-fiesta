
def move_zeros(lst):
  c = 0
  a = []
  for x in lst:
    if x == 0 and type(x) != bool:
      c += 1
    else:
      a.append(x)
  return a + [0] * c

