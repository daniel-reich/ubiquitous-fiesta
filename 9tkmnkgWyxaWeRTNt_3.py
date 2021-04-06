
def median(lst):
  size = len(lst)
  lst.sort()
  
  if size % 2 == 0:
    return (lst[size//2 - 1] + lst[size//2])/2
  else:
    return lst[size//2]

