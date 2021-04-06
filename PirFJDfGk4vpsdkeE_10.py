
def help_bobby(size):  
    array = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        array[i][i] = 1
        array[size-i-1][i] = 1
    return array

