
def divide(lst, n):
  res = []
  toadd = []
  for item in lst:
    if sum(toadd) + item <= n:
      toadd.append(item)
    else:
      res.append(toadd)
      toadd = [item]
      
  res.append(toadd)
  return res

