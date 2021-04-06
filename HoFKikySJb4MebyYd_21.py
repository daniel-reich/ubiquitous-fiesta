
def transform_matrix(lst):
  new=[[0] * len(lst[0]) for r in range(len(lst))]
  for rn in range(len(new)):
    for cn in range (len(new[0])):
      for c in range(len(lst[0])):
        if c!=cn:
          new[rn][cn]+= lst[rn][c]
      for r in range(len(lst)):
        if r!=rn:
          new[rn][cn]+=lst[r][cn]
  return(new)

