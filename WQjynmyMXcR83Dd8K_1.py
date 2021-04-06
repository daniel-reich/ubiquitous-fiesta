
def number_of_swaps(lst):
  count = 0
  while len(lst)> 1:
    count += (len(lst)- 1 - lst.index(max(lst)))
    lst.remove(max(lst))
  return count

