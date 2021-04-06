
def cutting_grass(lst, *cuts):
  res = []
  for cut in cuts:
    for i in range(len(lst)):
      lst[i] -= cut
    res.append(lst[:])
  return [heights if min(heights) > 0 else 'Done' for heights in res]

