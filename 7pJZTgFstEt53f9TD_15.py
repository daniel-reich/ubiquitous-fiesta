
def transpose_matrix(lst):
  ret = []
  for i in range(len(lst[0])):
    sub = []
    for j in range(len(lst)):
      sub.append(lst[j][i])
    ret.append(sub)
  return ret

