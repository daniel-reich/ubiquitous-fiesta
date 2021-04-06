
def rotate_matrix(matrix, turns=1):
    while abs(turns) != 0:
        new = []
        if turns > 0:
            turns -= 1
            for row in range(0, len(matrix[0])):
                b = []
                for col in range(len(matrix)-1 ,-1, -1):
                    b.append(matrix[col][row])
                else:
                    new.append(b)
            matrix = new
        else:
            turns += 1
            for row in range(-1, -len(matrix[0])-1, -1):
                b = []
                for col in range(0, len(matrix)):
                    b.append(matrix[col][row])
                else:
                    new.append(b)
            matrix = new
    return matrix

