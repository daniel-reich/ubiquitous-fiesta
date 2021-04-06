
def accumulating_list(lst):
  sum=0
  list=[]
  for i in lst:
    sum+=i
    list.append(sum)
  return list

