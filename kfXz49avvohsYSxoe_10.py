
def binary_search(lst, left, right, elem):
  middle = (left+right) // 2
  if right >= left:
    if lst[middle] == elem:
      return True
    elif lst[middle] > elem:
      return binary_search(lst, left, middle-1, elem)
    else:
      return binary_search(lst, middle+1, right, elem)
  else:
    return False

