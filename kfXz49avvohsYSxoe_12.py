
def binary_search(lst, left, right, elem):
  if left >= right:
    return False
​
  mid = left + (right - left) // 2
  
  if lst[mid] == elem:
    return True
  
  if lst[mid] > elem:
    return binary_search(lst, left, mid, elem)
  
  if lst[mid] < elem:
    return binary_search(lst, mid + 1, right, elem)
  
  return False

