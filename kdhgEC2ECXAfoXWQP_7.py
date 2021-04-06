
def transpose_matrix(mtx):
  words_lst = []
  count = 0
  col = 0
  row = 0
  while count < len(mtx) * len(mtx[0]):
    if col == len(mtx):
      col = 0
      row += 1
    words_lst.append(mtx[col][row])
    col += 1
    count += 1
  return " ".join(words_lst)

