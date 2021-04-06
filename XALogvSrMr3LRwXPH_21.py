
def is_shuffled_well(lst):
  for i in range(len(lst)-2):
    if(abs(lst[i] - lst[i+1]) == 1 and abs(lst[i+1] - lst[i+2]) == 1):
      return False
  return True

