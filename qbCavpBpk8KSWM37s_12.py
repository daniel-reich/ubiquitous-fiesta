
def largest_gap(lst):
  lst = sorted(lst)
  gap = 0
  for i in range(len(lst)-1):
    if lst[i+1]-lst[i]>gap:
      gap = lst[i+1]-lst[i]
  return gap

