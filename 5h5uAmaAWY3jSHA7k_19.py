
def landscape_type(lst):
  if len(lst) < 3: return 'neither'
  i = 1
  while lst[i] == lst[i-1]:
    i += 1
    if i == len(lst) - 1: return 'neither'
  slope = lst[i] > lst [i-1]
  i += 1
  while lst[i] == lst [i-1] or ((lst[i] > lst[i-1]) == slope):
    i += 1
    if i == len(lst): return 'neither'
  while lst[i] == lst [i-1] or ((lst[i] < lst[i-1]) == slope):
    i += 1
    if i == len(lst): return 'mountain' if slope else 'valley'
  return 'neither'

