
def num_grid(lst):
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      count=0
      if (lst[i][j]!="#"):
        for k in range(i-1,i+2):
          for l in range(j-1,j+2):
            if (k>-1 and k<len(lst) and l>-1 and l<len(lst[0]) and lst[k][l]=="#"):
              count+=1
        lst[i][j]=str(count)
  return lst

