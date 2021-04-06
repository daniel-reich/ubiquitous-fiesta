
def switch_gravity_on(lst):
    gravityOn = [['-' for i in range(len(lst[0]))] for x in range(len(lst))]
    for column in range(len(lst[0])):
        blockCount = 0
        for tile in range(len(lst)):
            if lst[tile][column]  is '#':
                blockCount += 1
        for block in range(blockCount):
            gravityOn[0 - (block + 1)][column] = '#'
    return gravityOn

