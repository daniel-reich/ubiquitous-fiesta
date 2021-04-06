
def find_missing(lst):
  if lst is None or len(lst) < 1: return False
  else:
    new = []
    lst = sorted(lst, key=len)
    for x in range(len(lst)):
      if len(lst[x]) < 1: return False
      else: new.append(len(lst[x]))
    return list(set(list(range(min(new), max(new)))) - set(new))[0]

