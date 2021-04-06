
def transpose_matrix(mtx):
  return " ".join(w for tup in list(zip(*mtx)) for w in tup)

