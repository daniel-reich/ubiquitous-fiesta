
def fire(matrix, coordinates):
    pos = {'A':0,'B':1,'C':2,'D':3,'E':4}
    y = pos[coordinates[0]]
    x = int(coordinates[1])-1
    if matrix[y][x] == "*":
        return "BOOM"
    return "splash"

