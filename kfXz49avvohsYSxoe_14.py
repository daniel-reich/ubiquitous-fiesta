
def binary_search(lst, left, right, elem):
  if left > right:
    return False
  mid = (left + right) // 2
  if lst[mid] < elem:
    left = mid + 1
  elif lst[mid] > elem:
    right = mid - 1
  else:
    return True
  return binary_search(lst, left, right, elem)

