
def antipodes_average(lst):
  mid = (len(lst) + 1) // 2
  lst1, lst2 = lst[:mid], lst[mid:]
  totals = [a + b for a,b in zip(lst1, lst2[::-1])]
  return [i/2 for i in totals]

