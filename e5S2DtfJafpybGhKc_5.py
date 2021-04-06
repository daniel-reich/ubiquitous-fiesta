
def rotate(mat):
    tpose = map(list, zip(*mat))
    return [x[::-1] for x in tpose]

