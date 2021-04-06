
def lower_triang(arr):
  
  index = 1
​
  for i in range(len(arr)):
    arr[i][index:] = [0] * (len(arr) - index)
    index += 1
​
  return arr

