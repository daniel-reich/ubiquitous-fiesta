
def almost_sorted(lst):
  def sf(lst):
    if len(set(lst)) != len(lst):
      return False
    v = [lst[i + 1] - lst[i] > 0 for i in range(len(lst) - 1)]
    return len(set(v)) == 1
  k = sorted(lst)
  if (lst == k) or (lst == k[::-1]):
    return False
  for i in range(len(lst)):
    lst1 = lst[:i] + lst[i + 1:]
    if sf(lst1):
      return True
  return False

