
def rotate(mat):
  final = []
  for i in range(len(mat)):
    final.append([mat[j][i] for j in reversed(range(len(mat)))])
  return final

