
def order_people(lst, people):
  mat=[]
  for row in range(lst[0]):
    mat.append([0 for col in range(lst[1])])
  if people>lst[0]*lst[1]:
    return('overcrowded')
  count=1
  for row in range(lst[0]):
    for col in range(lst[1]):
      if count<=people:
        if (row+1)%2==1:
          mat[row][col]=count
          count+=1
        if (row+1)%2==0:
          mat[row][lst[1]-1-col]=count
          count+=1
  return(mat)

