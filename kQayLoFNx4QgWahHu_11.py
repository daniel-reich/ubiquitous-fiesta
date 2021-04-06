
def order(lst):
  lst_with_index = [(a, i) for i, a in enumerate(lst)]
  res = []
  for pair in sorted(lst_with_index, key=lambda x: x[0]):
    res.append(pair[1])
  return res

