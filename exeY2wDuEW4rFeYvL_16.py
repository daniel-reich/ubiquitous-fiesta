
def ordered_matrix(a, b):
  k = 1
  list = []
  for i in range(0,a):
    list.append([])
    for j in range(0,b):
      list[i].append(k)
      k += 1
  return list

