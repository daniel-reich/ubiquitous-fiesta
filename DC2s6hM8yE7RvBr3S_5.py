
def subtract_matrix(lst1, lst2):
  output=[] 
  for i in range(0,len(lst1)):
    output.append(lst1[i])
  for i in range(0,len(lst1)):
    for j in range(0,len(lst1[0])):
      output[i][j] = float(lst1[i][j]) - float(lst2[i][j])
  return output

