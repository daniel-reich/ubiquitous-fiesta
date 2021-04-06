
def transform_matrix(lst):
  arr=[]
  for i in range(len(lst)):
    temp=[]
    for j in range(len(lst[0])):
      temp.append(0)
    arr.append(temp)
  
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      count=0
      for k in range(len(lst[0])):
        if lst[i][k]==1 :
          count+=1
      for l in range(len(lst)):
        if lst[l][j]==1:
          count+=1
      if lst[i][j]==1:
        arr[i][j]=count-2
      else:
        arr[i][j]=count
  return arr

