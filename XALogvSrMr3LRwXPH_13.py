
def is_shuffled_well(lst):
  count = 0
  count_desc = 0
  for i in range(len(lst)-1):
    if lst[i] + 1 == lst[i+1]:
      count += 1
    else:
      count = 0
    if count == 2:
      return False
    if lst[i] - 1 == lst[i+1]:
      count_desc += 1
    else:
      count_desc = 0
    if count_desc == 2:
      return False
  return True

