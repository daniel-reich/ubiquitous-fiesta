
def median(lst):
  lst = sorted(lst)
  middleIndex = len(lst) // 2
  if (len(lst) % 2 == 1):
    return lst[middleIndex]
  else: 
    return (lst[middleIndex] + lst[middleIndex-1]) / 2

