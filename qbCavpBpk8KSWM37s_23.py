
def largest_gap(lst):
  return max([sorted(lst)[i]-sorted(lst)[i-1]  for i in range(1,len(lst))])

