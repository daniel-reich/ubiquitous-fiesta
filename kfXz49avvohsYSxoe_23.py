
def binary_search(lst, left, right, elem):
  if left > right:
    return False
  middle = (left + right) // 2
  if lst[middle] < elem:
    left = middle + 1
  elif lst[middle] > elem:
    right = middle - 1
  elif lst[middle] == elem:
    return True
  return binary_search(lst, left, right, elem)

