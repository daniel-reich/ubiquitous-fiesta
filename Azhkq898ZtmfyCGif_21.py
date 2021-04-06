
def numbers_to_ranges(lst):
  res, cur = [], []
  for i in lst + [0]:
    if not cur: cur = [i, i]
    elif i == cur[1] + 1: cur[1] = i
    else: res.append(cur); cur = [i, i]
  return [('{}' + '-{}'*(a != b)).format(a, b) for a, b in res]

