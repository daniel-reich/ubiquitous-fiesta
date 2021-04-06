
def transpose_matrix(mtx):
  columns_count  = len(mtx[0])
  return " ".join(row[column] for column in range(0, columns_count) for row in mtx);

