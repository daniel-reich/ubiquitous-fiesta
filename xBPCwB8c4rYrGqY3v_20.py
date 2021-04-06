
def missing(lst):
  lst.sort()
  gap = max(lst)
  for i in range(1, len(lst)):
    if lst[i] - lst[i-1] < gap:
      gap = lst[i] - lst[i-1]
  for i in lst:
    if i + gap not in lst:
      return i + gap

