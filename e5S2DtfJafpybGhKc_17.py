
def rotate(mat):
    return [row[::-1] for row in [list(i) for i in zip(*mat)]]

