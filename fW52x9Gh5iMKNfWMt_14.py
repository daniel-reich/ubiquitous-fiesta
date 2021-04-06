
def recaman_index(n):
  res = [0]
  while res[-1] != n:
    sub = res[-1]-len(res); add = res[-1]+len(res)
    if sub > 0 and sub not in res:
      res.append(sub)
    else:
      res.append(add)
  return len(res)-1

