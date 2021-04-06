
def multiply(l):
  
  lst_nested=[]
  for i in l:
    lst=[]
    for j in range(len(l)):
      lst.append(i)
    lst_nested.append(lst)
  return lst_nested

