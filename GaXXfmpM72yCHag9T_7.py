
def unique(lst):
  for item in lst:
    if lst.count(item) == 1:
      return item

