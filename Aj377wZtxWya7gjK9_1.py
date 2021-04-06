
def sum_missing_numbers(lst):
  
  tr = 0
  
  for n in range(min(lst), max(lst) + 1):
    if n not in lst:
      tr += n
  
  return tr

