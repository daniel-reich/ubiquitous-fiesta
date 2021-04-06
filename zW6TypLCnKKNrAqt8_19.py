
def left_side(lst):
  arr = len(lst) * [0]
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if lst[j] > lst[i]:
        arr[j] += 1
  return arr
  
​
def right_side(lst):
  return left_side(lst[::-1])[::-1]

