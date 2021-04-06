
def sum_of_slices(lst):
  i, a, res = 0, [], 0
  for i in range(len(lst)):
    if res + lst[i] > 100:
      a.append(res)
      res = 0
    res += lst[i]
  a.append(res)
  return a

