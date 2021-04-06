
def sorting_steps(lst):
  lst = lst[:]; res = []
  for i in range(len(lst)):
    if lst[i] == sorted(lst)[i]:
      pass
    else:
      j = lst[i:].index(min(lst[i:]))+i
      lst[i], lst[j] = lst[j], lst[i]
      res.append((i,j))
  return res

