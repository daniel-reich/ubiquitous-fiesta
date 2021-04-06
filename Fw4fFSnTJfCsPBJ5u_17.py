
def how_many_missing(lst):
  return 0 if not lst else lst[-1]-lst[0]-len(lst)+1

