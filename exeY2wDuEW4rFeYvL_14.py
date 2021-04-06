
def ordered_matrix(a, b):
  v, res = 1, []
  for y in range(a):
    temp = []
    for x in range(b):
      temp.append(v)
      v += 1
    res.append(temp)
  return res

