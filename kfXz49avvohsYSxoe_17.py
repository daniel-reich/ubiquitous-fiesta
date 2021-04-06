
def binary_search(lst, left, right, elem):
  if left>right:
    return False
  mid=(left+right)//2
  if lst[mid]==elem:
    return True
  elif lst[mid]>elem:
    return binary_search(lst,left,mid-1,elem)
  else:
    return binary_search(lst,mid+1,right,elem)

