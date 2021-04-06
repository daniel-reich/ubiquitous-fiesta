
def matrix_multiply(a, b):
  trb=[list(x) for x in zip(*b)]
  if len(a[0])==len(b):
    res=[[0 for j in range(len(b[0]))] for i in range(len(a))]
    for i in range(len(res)):
      for j in range(len(res[0])):
        res[i][j]=sum(a[i][k]*trb[j][k] for k in range(len(a[0])))
    return res      
  else:
    return "invalid"

