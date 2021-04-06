
def largest_gap(lst):
  lst.sort()
  return max([b - a for a, b in zip(lst, lst[1:])])

