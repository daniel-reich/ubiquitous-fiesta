
def binary_search(lst, left, right, elem):
  while left <= right:
    m = (left + right)//2
    if lst[m] == elem:
      return True
    elif lst[m] > elem:
      right = m - 1
    elif lst[m] < elem:
      left = m + 1
  return False

