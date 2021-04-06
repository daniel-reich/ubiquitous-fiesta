
def binary_search(lst, left, right, elem):
  while left <= right:
    mid = (left + right)//2
    if lst[mid] == elem: return True
    if lst[mid] < lst[right]:
      left += 1
    else:
      right -=1 
  return False

