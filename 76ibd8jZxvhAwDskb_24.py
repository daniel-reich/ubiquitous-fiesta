
def tallest_skyscraper(lst):
  height = len(lst)
  for row in lst:
    if 1 in row:
      return height
    height -= 1

