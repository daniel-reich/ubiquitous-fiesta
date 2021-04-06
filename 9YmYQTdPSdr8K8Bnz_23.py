
def unique_lst(lst):
  l = [x for x in lst if x > 0]
  y = []
  for x in l:
    if x not in y:
      y.append(x)
  return y

