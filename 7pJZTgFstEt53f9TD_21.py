
def transpose_matrix(lst):
  tr = []
  for n in range(0, len(lst[0])):
    t = []
    for row in lst:
      t.append(row[n])
    tr.append(t)
  return tr

