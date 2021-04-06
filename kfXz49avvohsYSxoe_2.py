
def binary_search(lst, left, right, elem):
  if left > right: return False
  middle=(left+right)//2
  if lst[middle]<elem: return binary_search(lst,middle+1,right,elem)
  elif lst[middle]>elem: return binary_search(lst,left,middle-1,elem)
  else: return True

