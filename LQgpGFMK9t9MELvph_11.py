
def get_diagonals(lst):
  ans=[]
  a=[]
  for i in range(len(lst)):
    a.append(lst[i][i])
  ans.append(a)
  b=[]
  for i in range(len(lst)):
    b.append(lst[i][-i-1])
  ans.append(b)
  return ans

