
def spiral_order(matrix):
    s = []
    while matrix:
        s += matrix.pop(0)
        matrix = list(map(list,zip(*matrix)))[::-1]
    return s

