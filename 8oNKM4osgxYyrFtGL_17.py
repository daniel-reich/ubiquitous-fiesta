
def multiply(arr):
  lst=[]
  for i in range(len(arr)):
    temp=[]
    for j in range(len(arr)):
      temp.append(arr[i])
    lst.append(temp)
  return lst

