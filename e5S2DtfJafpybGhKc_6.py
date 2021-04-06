
def rotate(mat):
  A=list(map(list,zip(*mat)))
  return [x[::-1] for x in A]

