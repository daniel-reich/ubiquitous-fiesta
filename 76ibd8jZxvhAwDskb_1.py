
def tallest_skyscraper(lst):
  return max(sum(i) for i in zip(*lst))

