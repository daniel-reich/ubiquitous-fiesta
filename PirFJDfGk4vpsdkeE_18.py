
def help_bobby(size):  
  array=[]
  for i in range(size):
    array.append(list([0]*size))
  for i in array:
    print(i)
  for c in range(size):
    array[c][c] = 1
    array[c][size-c-1] = 1
  return array

