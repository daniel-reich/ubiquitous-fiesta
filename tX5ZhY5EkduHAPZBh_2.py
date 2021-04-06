
def nearest_element(n, lst):
  difference = [abs(n-x) for x in lst]
  
  if difference.count(min(difference)) == 1:
    return difference.index(min(difference))
  else:
    nearest = []
    for x in lst:
      if abs(n-x) == min(difference):
        nearest.append(x)
  return lst.index(max(nearest))

