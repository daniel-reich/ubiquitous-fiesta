
def min_length(lst, n):
  subs = []
  for i in range(len(lst)):
    sub = []
    j = i
    s = 0
    while j < len(lst):
      s += lst[j]
      sub.append(lst[j])
      if s > n:
        subs.append((len(sub),sub))
        break
      j += 1
  subs.sort()
  if len(subs) == 0:
    return -1
  return subs[0][0]

