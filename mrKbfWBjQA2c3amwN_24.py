
def mult_table(n):
  myans = []
  for i in range(1,n+1):
    temp = []
    for j in range(1,n+1):
      temp.append(i*j)
    myans.append(temp)
  return myans

