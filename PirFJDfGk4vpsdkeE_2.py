
def help_bobby(size):  
    array=[[0]*size for _ in range(size)]
    for i in array:print(i)
    row=0
    for column in range(size):
        array[row][column]=1
        array[row][size-column-1]=1
        row+=1
    for i in array:print(i)
    return array
​
'''
def help_bobby(size):
    """
    My preferred method
    """
    return [[1 if i==j or i+j==size-1 else 0 for j in range(size)] \
            for i in range(size)]
'''

