
def binary_search(lst, left, right, elem):
  if left > right:
    return False
  middle = (left + right) // 2
  if lst[middle] == elem:
    return True
  if elem > lst[middle]:
    return binary_search(lst,middle + 1 , right, elem)
  if elem < lst[middle]:
    return binary_search(lst, left, middle - 1, elem)

