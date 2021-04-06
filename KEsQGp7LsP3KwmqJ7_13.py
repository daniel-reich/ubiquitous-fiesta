
def check(lst):
  if lst == sorted(lst):
    return "NO"
  so = sorted(lst)
  i = lst.index(so[0])
  lst2 = lst[i:] + lst[:i]
  if lst2 == so:
    return "YES"
  return "NO"

