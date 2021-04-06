
def leader(lst):
  greater = []
  for i in range(len(lst)):
    if all(lst[i] > x for x in lst[i+1:]):
      greater.append(lst[i])
  return greater

