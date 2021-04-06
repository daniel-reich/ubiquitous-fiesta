
def ones_infection(arr):
​
  col_indexes = []
  row_indexes = []
​
  for n in range(len(arr)):
    for num in range(len(arr[n])):
      item = arr[n][num]
      if item == 1:
        col_indexes.append(num)
        row_indexes.append(n)
  
  rl = len(arr[0])
  
​
  for n in range(0, len(arr)):
    if n in row_indexes:
      for num in range(0, rl):
        arr[n][num] = 1
    else:
      for num in range(0, rl):
        if num in col_indexes:
          arr[n][num] = 1
          
  return arr

