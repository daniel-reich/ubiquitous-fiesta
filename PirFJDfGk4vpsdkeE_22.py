
def help_bobby(size):
    array=[[0 for _ in range(size)]for _ in range(size)]
    row=0
    for column in range(size):
        array[column][row]=1
        array[size-1-column][row]=1
        row+=1
    return array

