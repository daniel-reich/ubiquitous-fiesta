
def little_big(n):
  res = []
  for i in range(n):
    if not i % 2:
      res.append(5 + i // 2)
    elif i == 1:
      res.append(100)
    else:
      res.append(res[i - 2] * 2)
  return res[-1]

