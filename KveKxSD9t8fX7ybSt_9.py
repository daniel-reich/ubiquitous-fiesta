
def final_countdown(lst):
  lsts = []
  tmp = []
  n = 0
  for x in lst:
    if not tmp or tmp[-1] - x == 1:
      tmp.append(x)
    else:
      tmp = [x]
    if x == 1:
      lsts.append(tmp)
      n += 1
  return [n, lsts]

