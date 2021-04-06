
def transpose_matrix(array):
​
  res = [] 
​
  for i in range(len(array[0])):
    temp = [] 
    for j in range(len(array)):
      temp.append(array[j][i])
    res.append(temp)
​
  return(res)

