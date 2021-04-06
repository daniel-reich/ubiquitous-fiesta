
def less_or_equal(lst, k):
  l = sorted(lst)
  return 1 if k == 0 and l[0] > 1 else None if len(l) == 1 and l[0] == 1\
      else l[:k][-1] if l[k:].count(l[:k][-1]) == 0  else None

