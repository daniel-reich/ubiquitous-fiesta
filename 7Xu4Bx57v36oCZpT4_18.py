
def where_is_waldo(lst):
  mylist =[]
  for i in range (len(lst)):
    for j in range (len(lst[i])):
      if(lst[i].count(lst[i][j])==1):
        return [i+1,j+1]               
  return None

