
def is_shuffled_well(lst):
  print(lst)
  for i in range(0, len(lst)-2):
    if (abs(lst[i] - lst[i + 1]) == 1 and abs(lst[i+1] - lst[i+2]) == 1):
      return False
  
  return True

