
def sum_missing_numbers(lst):
  c, total = min(lst), 0
  
  while c < max(lst):
    if c not in lst:
      total += c
    c += 1
  
  return total

