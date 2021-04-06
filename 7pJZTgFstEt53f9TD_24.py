
def transpose_matrix(lst):
  tp = []
  for p in range(len(lst[0])):
    tp.append([a[p] for a in lst])
  return tp

