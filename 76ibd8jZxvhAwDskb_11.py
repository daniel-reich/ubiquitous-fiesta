
def tallest_skyscraper(lst):
  length = []
  for x in range(len(lst)):
    if 1 in lst[x]:
      length.append(x)
  return(len(length))

