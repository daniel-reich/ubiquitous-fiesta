
def delete_occurrences(lst, num):
  d = {}
  ans = []
  c = 0
  for i in lst:
    if i in d:
      c = ans.count(i)
    if i not in d:
      c = 0
    d[i] = c
    if c < num:
      ans.append(i)
  return ans

