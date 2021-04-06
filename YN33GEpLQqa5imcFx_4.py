
def pascals_triangle(row):
  r=[1]
  for i in range(1,row+1): r+=[r[i-1]*(row+1-i)//i]
  return ' '.join(map(str,r))

