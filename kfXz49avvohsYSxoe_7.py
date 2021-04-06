
def binary_search(lst, left, right, elem):
  mid = right + left
  mid //= 2
  if right == left:
    return lst[right] == elem
  if lst[mid] == elem:
    return True
  if lst[mid] > elem:
    return binary_search(lst, left, mid-1, elem)
  else:
    return binary_search(lst, mid+1, right, elem)

