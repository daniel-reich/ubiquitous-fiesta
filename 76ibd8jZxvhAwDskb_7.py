
def tallest_skyscraper(lst):
  for i in range(len(lst)):
    if sum(lst[i]) > 0:
      return (len(lst) - i)

