
def help_bobby(size):  
  array = [[0 for i in range(size)] for i in range(size)]
  for column in range(size):
    array[column][column]=1
    array[column][-column - 1]=1
  return array

