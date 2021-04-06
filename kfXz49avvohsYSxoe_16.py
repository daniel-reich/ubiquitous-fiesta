
def binary_search(lst, left, right, elem):
  ndx = (left+right)//2
  
  if lst[ndx] == elem:
    return True
  elif lst[ndx] > elem:
    right = ndx
  elif lst[ndx] < elem:
    left = ndx
  
  if abs(right-left) < 2:
    return False
​
  return binary_search(lst,left,right,elem)

