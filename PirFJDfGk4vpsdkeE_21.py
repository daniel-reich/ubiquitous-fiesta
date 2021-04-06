
def help_bobby(size):
    array = []
    for i in range(size):
        sub = [0 for i in range(size)]
        array.append(sub)
​
    row = 0
    for column in range(size):
        array[column][row] = 1
        array[(size - 1) - column][row] = 1
        row += 1
        
    return array

