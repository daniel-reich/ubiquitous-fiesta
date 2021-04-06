
def missing(lst):
  k = [lst[i] - lst[i - 1] for i in range(1, len(lst))]
  kst = max(k)
  for i in range(1, len(lst)):
    if lst[i] - lst[i - 1] == kst:
      return lst[i - 1] + min(k)
  return None

