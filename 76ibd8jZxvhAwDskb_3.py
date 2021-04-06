
def tallestSkyscraper(lst):
  for i in range(len(lst)):
    if lst[i].count(1):
      return len(lst) - i

