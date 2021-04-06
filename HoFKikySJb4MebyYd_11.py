
def transform_matrix(lst):
  nlst = list()
  for rnum in range(len(lst)):
    nlst.append(list())
    for cnum in range(len(lst[-1])):
      nlst[-1].append(lst[rnum].count(1)+[lst[x][cnum] for x in range(len(lst))].count(1)-(2*lst[rnum][cnum]))
  return nlst

