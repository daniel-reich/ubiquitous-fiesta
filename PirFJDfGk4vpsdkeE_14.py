
def help_bobby(size):  
    array = [[0] * size for i in range(size)]
    row = 0
    for column in range(size):
        array[row][column] = 1
        array[row][size - column - 1] = 1
        row += 1
    return array

