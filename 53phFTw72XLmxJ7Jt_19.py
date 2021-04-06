
def marathon_distance(d): 
  a1 = []
  for num in d:
    a1.append(abs(num))
  if sum(a1)==25:
    return True
  else:
    return False

