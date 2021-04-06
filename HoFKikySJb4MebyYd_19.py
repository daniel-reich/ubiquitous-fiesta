
def transform_matrix(lst):
  row_sums = [sum(r) for r in lst]
  col_sums = [sum([r[i] for r in lst]) for i in range(len(lst[0]))]
  out = []
  for i in range(len(lst)):
    out_r = []
    out.append(out_r)
    for j in range(len(lst[0])):
      out_r.append(row_sums[i] + col_sums[j] - 2* lst[i][j] )
  return out

