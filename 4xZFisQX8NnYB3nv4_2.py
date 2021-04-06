
def maximum_seating(lst):
  l = len(lst)
  count = 0
  for i, v in enumerate(lst):
    if v == 0 and \
      (i - 2 < 0 or lst[i - 2] != 1) and \
      (i - 1 < 0 or lst[i - 1] != 1) and \
      (i + 2 >= l or lst[i + 2] != 1) and \
      (i + 1 >= l or lst[i + 1] != 1):
      lst[i] = 1
      count += 1
  return count

