
def help_bobby(size):  
    array=[[0 for j in range(size)]for i in range(size)]
    for i in array:print(i)
    for column in range(size):
      array[column][column]=1
      array[size-column-1][column]=1
    for i in array:print(i)
    return array

