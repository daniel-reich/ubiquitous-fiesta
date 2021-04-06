
def tallest_skyscraper(lst):
  maxtall = len(lst)
  for i in range(maxtall-1):
    if 1 not in lst[i]:
      maxtall -= 1
    else:
      return maxtall

