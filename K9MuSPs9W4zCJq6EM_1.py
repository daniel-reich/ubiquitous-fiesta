
def cycle_length(lst, n):
  l = 0
  s = sorted(lst)
  j, k = lst.index(n), s.index(n)
  while j != k:
    k = s.index(lst[k])
    l += 1
  return l

