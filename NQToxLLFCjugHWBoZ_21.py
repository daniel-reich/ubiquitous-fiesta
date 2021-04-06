
def sort_by_character(lst, n):
  A=sorted([(x[n-1],x) for x in lst])
  return [x[1] for x in A]

