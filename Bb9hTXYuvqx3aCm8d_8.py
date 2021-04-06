
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  rem_A=[str_A[i] for i in range(len(str_A)) if i not in ind_Z]
  rem_Z=[str_Z[i] for i in range(len(str_Z)) if i not in ind_A]
  ord_A=[ord(rem_A[i]) for i in range(len(rem_A))]
  ord_Z=[ord(rem_Z[i]) for i in range(len(rem_Z))]
  point_A=[]
  point_Z=[]
  for x,z in zip(ord_A, ord_Z):
    if x>=z:
      point_A.append(x-z)
    else:
      point_Z.append(z-x)
  return  { "A": sum(point_A), "Z": sum(point_Z) }

