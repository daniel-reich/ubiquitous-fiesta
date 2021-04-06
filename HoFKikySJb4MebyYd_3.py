
def transform_matrix(lst):
  return [[sum(lst[r]) + sum(list(zip(*lst))[c]) - lst[r][c] * 2 for c in range(len(lst[r]))] for r in range(len(lst))]

