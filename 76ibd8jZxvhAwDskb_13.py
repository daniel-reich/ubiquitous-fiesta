
def tallest_skyscraper(lst):
  output = []
  tallest = 0
  for i in range(len(lst)):
    for j in lst[i]:
      if j != 0:
        output.append([i,j])
  low = len(lst)
  for i,j in output:
    if i < low:
      low = i
  return len(lst)-low

