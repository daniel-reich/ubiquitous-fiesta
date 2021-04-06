
def help_bobby(size):
    #array=[[[0]*size]*size]---->1 x size array, should be size x size
    array=[[0 for x in range(size)] for y in range(size)]
    for i in array:print(i)
    row=0
    for column in range(size):
        array[column][row]=1
        #array[size-column][row]=1---->size-1 is largest index
        array[size-1-column][row]=1
        row+=1
    for i in array:print(i)
    return array

