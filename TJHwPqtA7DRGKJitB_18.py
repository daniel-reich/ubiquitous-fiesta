
def is_prob_matrix(array):
  if len(array) == len(array[0]):
    for i in range(0, len(array)):
      total = 0
      for j in range(0, len(array[i])):
        if array[i][j] >= 0:
          total += array[i][j]
      if total != 1:
        return False
    return True
​
  else:
    return False
    
print(is_prob_matrix([[0.5, 0.5, 0.0], [0.2, 0.5, 0.3],[0.1, 0.2, 0.7]]))

