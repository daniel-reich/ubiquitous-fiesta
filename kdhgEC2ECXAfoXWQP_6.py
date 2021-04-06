
def transpose_matrix(mtx):
  return " ".join(" ".join(i) for i in list(map(list,zip(*mtx))))

