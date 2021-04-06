
def transform_matrix(lst):
  ans=[0]*len(lst)
  for i in range(len(ans)):
    ans[i]=[0]*len(lst[0])
  for i in range(len(lst)):
    for x in range(len(lst[i])):
      count=0
      count+=lst[i].count(1)
      count+=[lst[a][x] for a in range(len(lst))].count(1)
      if lst[i][x]==1: count-=2
      ans[i][x]=count
  for i in lst: 
    print(i)
  for i in ans:
    print(i)
  return ans

