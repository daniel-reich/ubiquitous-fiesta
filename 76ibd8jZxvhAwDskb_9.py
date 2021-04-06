
def tallest_skyscraper(lst):
  for i in range(0, len(lst)):
    if 1 in lst[i]:
      return len(lst) - i

