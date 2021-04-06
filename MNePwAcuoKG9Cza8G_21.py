
def build_staircase(height, block):
    if height == 0:
        return []
    column = 0
    row = 0
    
    a = [['_' for i in range(0 , height)] for j in range(height)]
    
    while True:
        for k in range(0 , column + 1):
            a[row][k] = block
        row += 1
        column += 1
        if column == height :
            break
    return a

