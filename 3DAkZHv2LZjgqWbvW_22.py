
def is_adjacent(matrix, node1, node2):
  if matrix[node1][node2] == 1 and matrix[node2][node1] == 1:
    return True
  return False

