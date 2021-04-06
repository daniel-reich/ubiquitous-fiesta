
def simple_pair(lst, n):
  a = []
  for i, j in enumerate(lst):
      if j!= 0 and n/j in (lst[:i]+lst[i+1:]):
          a.append([j, n/j])
          break
  return None if not a else a[0]

