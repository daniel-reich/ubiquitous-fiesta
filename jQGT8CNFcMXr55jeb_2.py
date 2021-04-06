
def numbers_sum(lst):
  x = [0]
  for i in lst:
    if type(i) == int:
      x.append(i)
  return sum(x)

