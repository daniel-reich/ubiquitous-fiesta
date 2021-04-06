
def recaman_index(n):
  lst = [0]
  while n not in lst:
    val = lst[-1] - len(lst)
    if val > 0 and val not in lst:
      lst.append(val)
    else:
      lst.append(lst[-1] + len(lst))
  return lst.index(n)

