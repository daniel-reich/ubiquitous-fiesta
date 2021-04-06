
def binary_search(lst, left, right, elem):
  boolean_condition = True
  while boolean_condition:
    middle = (left + right) // 2
    if left > right:
      return False
    elif lst[middle] < elem:
      left = middle + 1
    elif lst[middle] > elem:
      right = middle - 1
    else:
      return True

