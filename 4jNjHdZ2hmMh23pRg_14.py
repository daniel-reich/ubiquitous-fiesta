
def cutting_grass(lst, *cuts):
  res = []
  for n in cuts:
    lst = [e-n for e in lst]
    if min(lst) < 1:
      res.append('Done')
    else:
      res.append(lst)
  return res

