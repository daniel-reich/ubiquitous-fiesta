
def delete_occurrences(lst, num):
  res = []
  for i in lst:
    if res.count(i) < num:
      res.append(i)
  return res

