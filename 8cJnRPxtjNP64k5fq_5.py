
def dance(lst,parameter):
  for i in range(len(lst)//2):
    if(parameter == 'women'):
      index = 0
    else:
      index = 1
​
    tmp = lst[i][index]
    lst[i][index] = lst[-(i+1)][index]      
    lst[-(i+1)][index] = tmp
    
  return lst

