
def help_bobby(size):  
    array=[a for a in [[0]*size for _ in range(size)]]
    for column in range(size):
        array[column][column]=1
        array[size - column - 1][column]=1
    for i in array:print(i)
    return array

