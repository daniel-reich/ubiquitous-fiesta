
def help_bobby(size):  
    array = [[0 for x in range(size)] for y in range(size)]
    for x in range(size):
        array[x][x] = 1
        array[size - x - 1][x] = 1
    return array

