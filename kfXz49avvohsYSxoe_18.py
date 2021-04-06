
def binary_search(lst, left, right, elem):
  if left > right:
    return False
  m = (left+right)//2
  if lst[m] == elem:
    return True
  elif lst[m] > elem:
    right = m-1
    return binary_search(lst, left, right, elem)
  elif lst[m] < elem:
    left = m+1
    return binary_search(lst, left, right, elem)

