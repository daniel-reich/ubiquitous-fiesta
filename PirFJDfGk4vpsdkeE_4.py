
def help_bobby(size):  
    array=[[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        array[i][i]=1
        array[size-1-i][i]=1
    return array

