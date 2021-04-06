
def find_missing(lst):
  if lst is None or [] in lst or lst == []:
    return False
  s = set(len(l) for l in lst)
  return (set(range(min(s), max(s)+1)) - s).pop()

