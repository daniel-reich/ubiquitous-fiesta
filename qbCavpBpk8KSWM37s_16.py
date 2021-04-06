
def largest_gap(lst):
  lst = sorted(lst)
  return max([lst[n+1] - lst[n] for n in range(len(lst) - 1)])

