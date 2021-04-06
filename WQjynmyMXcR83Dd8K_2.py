
def number_of_swaps(lst):
  return sum(sum(lst[x] > y for y in lst[x+1:]) for x in range(len(lst)))

