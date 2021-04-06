
def largest_gap(lst):
  lst = sorted(set(lst))
  return max(b-a for a,b in zip(lst, lst[1:]))

