
def tallest_skyscraper(lst):
  for stuff in range(0,len(lst)):
    if lst[stuff].count(1) > 0:
      return len(lst)-stuff
  return 0

