
def divide(lst, n):
  res = [[]]
  for i in lst:
    if sum(res[-1]) + i > n:
      res.append([i])
    else:
      res[-1].append(i)
  return res

