
def is_shuffled_well(lst):
  for i in range(1, len(lst)-1):
    if abs(lst[i+1] - lst[i]) == 1 and abs(lst[i] - lst[i-1]) == 1:
      return False
  return True

