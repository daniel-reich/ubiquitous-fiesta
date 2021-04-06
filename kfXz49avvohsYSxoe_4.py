
def binary_search(lst, left, right, elem):
  search = True
  while search:
    middle = right + left // 2
    if left > right:
      search = False
      
    elif lst[middle] < elem:
      left = middle + 1
​
    elif lst[middle] > elem:
      right = middle - 1
​
    elif lst[middle] == elem:
      return True
  return False

