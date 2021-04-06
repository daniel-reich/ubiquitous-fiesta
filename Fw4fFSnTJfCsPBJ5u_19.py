
def how_many_missing(lst):
  try:
    return len([i for i in range(lst[0],lst[-1]+1) if i not in lst])
  except IndexError:
    return 0

