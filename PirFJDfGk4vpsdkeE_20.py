
def help_bobby(size):  
    # List comprehension updated due to Python's memory handling.
    array=[[0 for _ in range(size)] for _ in range(size)]
    for i in array:print(i)
    row=0
    for column in range(size):
        array[column][row]=1
        array[size-column-1][row]=1 # Indexes need to be zero-indexed
        row+=1
    for i in array:print(i)
    return array

