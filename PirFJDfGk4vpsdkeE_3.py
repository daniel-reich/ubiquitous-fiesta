
def help_bobby(size):  
  array=[]
  
  for i in range(size):
    array.append([0] * size)
  
  for i in range(size):
    array[i][i]=1
    array[i][size-1-i]=1
    
​
  return array

