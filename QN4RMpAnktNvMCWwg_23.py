
def id_mtrx(n):
  if str(n).replace('-','').isdigit():
    L0 = [[0 for i in range(abs(n))] for u in range(abs(n))]
  else:
    return "Error"
  for i in range(len(L0[0])):
    if n > 0:
      L0[i][i]=1
    if n < 0:
      L0[(i+1)*-1][i]=1 
  # 0 1 2 3 4 5 
  # -1-2-3-4-5-6  
  return L0

