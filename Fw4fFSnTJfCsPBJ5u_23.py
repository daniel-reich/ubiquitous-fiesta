
def how_many_missing(lst):
  length = len(lst)
  return 0 if length == 0 else len(range(lst[0], lst[length-1]+1)) - length

