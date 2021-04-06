
def to_list(dct):
  lst = []
  sortedDict = sorted(dct.keys())
  for k in sortedDict:
    lst.append([k, dct[k]])
  return lst

