
def sum_even_nums_in_range(start, stop):
  count = 0
  for x in range(start, stop+1):
    if x%2 == 0 : 
      count = count + x
  return count

