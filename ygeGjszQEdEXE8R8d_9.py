
offsets = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
​
def position_of_one(matrix):
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if el == 1:
                return i, j
​
def move(mat):
    def change(action):
        nonlocal mat
        if action == "stop":
            return mat
        i, j = position_of_one(mat)
        offset = offsets[action]
        dim1, dim2 = len(mat), len(mat[0])
        mat = [[0] * dim2 for row in mat]
        mat[(i + offset[0]) % dim1][(j + offset[1]) % dim2] = 1
        return change
    return change

