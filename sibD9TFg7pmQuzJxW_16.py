
def stem_plot(lst):
  res, stem = [], -1
  for s, l in  sorted([divmod(val, 10) for val in lst]):
    if s != stem:
      res.append([s, [str(l)]])
      stem = s
    else:
      res[-1][1].append(str(l))
  return ["{} | {}".format(s, ' '.join(lvs)) for s, lvs in res]

