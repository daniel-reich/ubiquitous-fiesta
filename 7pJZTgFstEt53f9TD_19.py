
import copy
def transpose_matrix(lst):
  rows = len(lst)
  cols = len(lst[0])
  new_lst = [[0 for x in range(rows)] for y in range(cols)]
  for row in range(len(lst)):
    for col in range(len(lst[0])):
      new_lst[col][row] = lst[row][col]
  return new_lst

