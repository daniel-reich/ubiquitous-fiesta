
def complete_square(arr):
  if len(arr[0])<len(arr):
    for i in range(len(arr)):
      arr[i]+=[0]*(len(arr)-len(arr[i]))
    return arr
  else:
    for i in range(len(arr[0])-len(arr)):
      arr.append([0]*len(arr[0]))
    return arr

