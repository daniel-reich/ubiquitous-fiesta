
def find_missing(lst):
  if None or not lst or lst.count([]) > 0:
    return False
  else:
    lens = [len(i) for i in lst]
    return list(set(range(min(lens), len(lst) + 2)) ^ set([len(i) for i in lst]))[0]

