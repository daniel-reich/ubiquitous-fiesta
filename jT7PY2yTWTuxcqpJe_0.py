
def spiral_order(matrix):
    if not matrix:
        return None
    path = []
    first_column = []
    while matrix:
        try:
            path += matrix.pop(0)
            for i in range(len(matrix)):
                path += [matrix[i].pop()]
                first_column.append(matrix[i].pop(0))
            path = path + matrix.pop()[::-1]
            path = path + first_column[::-1]
            first_column = []
        except:
            if first_column:
                path += firstcolumn
    return path

