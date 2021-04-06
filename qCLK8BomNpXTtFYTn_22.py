
def cumulative_sum(lst):
  cumsum = 0
  cumlist = []
  for i in lst:
    cumsum += i
    cumlist.append(cumsum)
  return cumlist

