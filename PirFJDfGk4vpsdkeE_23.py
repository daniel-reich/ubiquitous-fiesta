
def help_bobby(size):
    array=[]
    for i in range(size):array.append([0]*size)
    for column in range(size):
        array[column][column]=1
        array[size-1-column][column]=1
    print(*array,sep='\n')
    return array

