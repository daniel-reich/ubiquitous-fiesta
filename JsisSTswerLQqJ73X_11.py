
def priority_sort(lst, s):
  if not lst:
    return []
  elif not s:
    return sorted(lst)
  elif all(list(map(lambda x: not x in lst, s))):
    return sorted(lst)
  else:
    lst1 = sorted(list(filter(lambda x: x in s,lst)))
    lst1.extend(sorted(list(filter(lambda x: not x in s,lst))))
    return lst1

