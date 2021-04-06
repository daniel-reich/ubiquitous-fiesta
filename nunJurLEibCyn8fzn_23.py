
def filter_list(lst):
  nlst = []
  for x in lst:
    if type(x) == int and x >= 0:
      nlst.append(x)
  return nlst

