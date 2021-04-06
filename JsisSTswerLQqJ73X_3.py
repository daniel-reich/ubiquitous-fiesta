
def priority_sort(lst, s):
  if lst:
    l=sorted([x for x in lst if x in s])
    A=sorted([x for x in lst if x not in l])
    return l+A
  return []

