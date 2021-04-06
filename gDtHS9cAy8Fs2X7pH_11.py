
def count_repetitions(lst):
  
  unique_items = list(set(lst))
  counted = {}
  
  for item in unique_items:
    counted[item] = lst.count(item)
  
  return counted

