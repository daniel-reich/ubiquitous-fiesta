
def spiral_order(matrix):
  lst = matrix[0]
  n = len(matrix[0])
  lst.extend([matrix[i][-1] for i in range(1,3)])
  lst.extend(matrix[2][-2::-1])
  lst.append(matrix[1][0])
  lst.extend(matrix[1][1:n-1])
  return lst

