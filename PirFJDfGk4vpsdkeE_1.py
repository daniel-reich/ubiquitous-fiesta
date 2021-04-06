
def help_bobby(size):  
    array=[[0 for i in range(size)] for i in range(size)]
    for i in array:print(i)
    row=0
    for column in range(size):
        array[column][row]=1
        array[size-column-1][row]=1
        row+=1
    for i in array:print(i)
    return array

