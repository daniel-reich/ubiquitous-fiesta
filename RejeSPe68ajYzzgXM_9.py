
def combine(lst):
  dct = {}
  for i in range(0, len(lst), 2):
    dct[lst[i][0]] = [lst[i][2], lst[i+1][2]]
  return dct

