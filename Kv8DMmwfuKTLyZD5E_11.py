
def make_dartboard(n):
  end,out,out1 = n//2 +1 if n%2==1 else n//2, [[1]*n],[]
  for i in range (1,end):
    row=[]
    positions=[i for i in range (n)]
    for j in range (i):
      positions.pop(0)
      positions.pop(-1)
    for k in range (n):
      if (k in positions):
        row.append(out[i-1][k]+1)
      else:
        row.append(out[i-1][k])
    out.append(row)
  for i in range (n//2-1,-1,-1):
    out.append(out[i])
  for i in range (len(out)):
    s=''
    for j in range (len(out)):
      s+=str(out[i][j])
    out1.append(int(s))
  return out1

