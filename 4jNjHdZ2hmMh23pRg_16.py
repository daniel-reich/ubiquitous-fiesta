
def cutting_grass(lst, *cuts):
  res = []
  for cut in cuts:
    cutting = [height-cut for height in lst]
    if all(height > 0 for height in cutting):
      res.append(cutting)
    else:
      res.append('Done')
    lst = cutting
  return res

