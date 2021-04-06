
def how_many_missing(lst):
  if not lst: return 0
  return max(lst)-min(lst)+1-len(lst)

