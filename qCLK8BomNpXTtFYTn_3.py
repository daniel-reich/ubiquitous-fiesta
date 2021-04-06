
def cumulative_sum(lst):
  total = 0
  lst2 = []
  for number in lst:
    total += number
    lst2.append(total) 
  return lst2

