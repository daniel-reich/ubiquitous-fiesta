
def is_shuffled_well(lst):
  for i in range(len(lst[:-2])):
    if abs(lst[i+1] - lst[i]) == 1:
      if lst[i+1] - lst[i] == lst[i+2] - lst[i+1]: return False
  return True

