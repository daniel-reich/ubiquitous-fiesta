
def help_bobby(size):
    arr = [[0 for _ in range(size)] for __ in range(size)]
    for i in range(size):
        arr[i][i] = 1
        arr[i][size-1-i] = 1
    return arr

