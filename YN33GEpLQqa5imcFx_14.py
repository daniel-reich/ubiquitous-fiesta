
def pascals_triangle(row):
    result = [1]
    bit = ""
    data = [[0 for i in range(row)] for j in range(row)]
    for i in range(row):
        data[0][i] = 1
        data[i][0] = 1
        
    for y in range(row - 1):
        for x in range(row - 1):
            data[y + 1][x + 1] = data[y + 1][x] + data[y][x + 1]
    for i in range(1, row):
        result.append(data[i][row - i])
    result.append(1)
    
    for i in result:
        bit += str(i) + " "
    return bit[ : - 1]

