
def mult_table(n):
  arr = []
  for i in range(n):
    temp = []
    for j in range(n):
      temp.append((i+1)*(j+1))
    arr.append(temp)
  return arr

