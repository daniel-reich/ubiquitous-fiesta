
def binary_search(list, left, right, elem):
  if(left == right):
    return (list[left] == elem)
  else:
    mid = (left+right)//2
    if(elem == list[mid]):
      return True
    elif (elem > list[mid]):
      return binary_search(list, mid+1, right, elem)
    else:
      return binary_search(list, left, mid-1, elem)

