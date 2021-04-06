
def determinant(A):
  return solve(A)
  
def solve(lst):
  if len(lst)==1 and len(lst[0])==1:
    return lst[0][0]
  elif len(lst)==2 and len(lst[0])==2:
    return (lst[0][0]*lst[1][1])-(lst[0][1]*lst[1][0])
  else:
    top,lst = lst[0],lst[1:]
    mlst = []
    for i in range(len(top)):
      mlst.append([x[:i]+x[i+1:] for x in lst])
    return sum([top[i]*solve(mlst[i]) for i in range(len(top)) if i%2==0])-sum([top[i]*solve(mlst[i]) for i in range(len(top)) if i%2==1])

