
def largest_gap(lst):
  lst.sort()
  return max(j-i for i,j in zip(lst,lst[1:]))

