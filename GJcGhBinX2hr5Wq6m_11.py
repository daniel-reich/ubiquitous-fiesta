
def move_zeros(lst):
  x = []
  x1 = []
  x2 = []
  for i in lst:
    if (i != 0 or str(i) == 'False'):
      x1.append(i)
    else:
      x2.append(i)
  return x1 + x2

