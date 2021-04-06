
def binary_search(lst, left, right, elem):
  if left > right:
    return False
  m = (left + right) // 2
  if lst[m] < elem:
    return binary_search(lst, m+1, right, elem)
  elif lst[m] > elem:
    return binary_search(lst, left, m-1, elem)
  return True

