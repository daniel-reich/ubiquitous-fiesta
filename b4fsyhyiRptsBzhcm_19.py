
def sum_even_nums_in_range(start, stop):
  total = 0
  if start % 2 != 0:
    start += 1
  for num in range(start, stop+1, 2):
    total += num
  return total

