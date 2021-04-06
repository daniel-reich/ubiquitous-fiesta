
def ascii_sort(lst):
  if sum([ord(x) for x in lst[0]]) > sum([ord(x) for x in lst[1]]):
    return lst[1]
  return lst[0]

