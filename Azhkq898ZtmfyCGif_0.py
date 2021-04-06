
def numbers_to_ranges(lst):
  if not lst: return []
  fst = lst.pop(0)
  curr = fst
  if not lst or curr+1 != lst[0]:
    return [str(fst)] + numbers_to_ranges(lst)
  while lst and curr+1 == lst[0]:
    curr = lst.pop(0)
  return ["{}-{}".format(fst,curr)] + numbers_to_ranges(lst)

