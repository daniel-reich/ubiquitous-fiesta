
def largest_gap(lst):
  lst=sorted(lst)
  return max([lst[i+1]-lst[i] for i in range(len(lst)-1)])

