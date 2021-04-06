
def ones_infection(arr):
  line_1_exists = []
  col_1_exists = []
  num_of_line = len(arr)
  num_of_col = len(arr[0])
  
  for i in range(num_of_line):
    line_1_exists.append(0)
  for j in range(num_of_col):
    col_1_exists.append(0)  
  
  for i in range(num_of_line):
    if 1 in arr[i]:
      line_1_exists[i] = 1
    for j in range(num_of_col):
      if arr[i][j] == 1:
        col_1_exists[j] = 1
​
  new_arr = arr
  for i in range(num_of_line):
    for j in range(num_of_col):
      if line_1_exists[i] == 1 or col_1_exists[j] == 1:
        new_arr[i][j] = 1
      else:
        new_arr[i][j] = 0
  return new_arr

