
def tallest_skyscraper(lst):
  return max([sum([lst[j][i] for j in range(len(lst))]) for i in range(len(lst[0]))])

