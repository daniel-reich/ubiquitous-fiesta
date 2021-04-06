
def transform_matrix(lst):
  res = []
  rot = list(map(list, zip(*lst)))
​
  for i in range(len(lst)):
    temp = []
    for j in range(len(lst[i])):
      r = sum(lst[i]) if lst[i][j] == 0 else sum(lst[i])-1
      c = sum(rot[j]) if lst[i][j] == 0 else sum(rot[j])-1
      temp += [r + c]
    res.append(temp)
  return res

