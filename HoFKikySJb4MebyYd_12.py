
def transform_matrix(lst):
  result = [[] for _ in range(len(lst))]
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      result[i].append(sum(lst[i])+sum([k[j] for k in lst])-2*lst[i][j])
  return result

