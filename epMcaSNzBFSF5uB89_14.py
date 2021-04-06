
def currently_winning(scores):
  y = [scores[0]]
  o =[]
  ys = scores[0]
  os = 0
  for i in range(1,len(scores)):
    if i%2 == 0:
      ys += scores[i]
      y.append(ys)
    else:
      os += scores[i]
      o.append(os)
  res = []
  for j in range(len(y)):
    if y[j] > o[j]:
      res.append('Y')
    if y[j] <o[j]:
      res.append('O')
    if y[j] == o[j]:
      res.append('T')
  return res

