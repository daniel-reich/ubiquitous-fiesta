
def tallest_skyscraper(lst):
  return max(len(lst) - lst.index(l) for l in lst if 1 in l)

