
def tallest_skyscraper(lst):
  return sum(1 for i in lst if sum(i)>0)

