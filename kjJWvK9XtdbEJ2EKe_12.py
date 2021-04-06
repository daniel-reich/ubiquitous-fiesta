
def sort_array(lst):
  ans = []
  while lst:
    m = lst[0]
    for x in lst:
      if x < m:
        m = x
    ans.append(m)
    lst.remove(m)
  return ans

