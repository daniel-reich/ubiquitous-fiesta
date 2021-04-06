
def get_indices(lst, el):
  res = []
  zipped = zip(lst, range(0, len(lst)))
  lst_zip = list(zipped)
  for i in range(0, len(lst)):
    if lst_zip[i][0] == el:
      res.append(lst_zip[i][1])
  return res

