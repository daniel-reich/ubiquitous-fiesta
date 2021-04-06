
def rotate(mat):
  return [[i[j] for i in mat][::-1] for j in range(len(mat))]

