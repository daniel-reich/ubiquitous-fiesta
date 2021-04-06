
def simon_says(lst1, lst2):
  result = list(zip(lst1, lst2))
  x,y = zip(*result)
  if x[0] == y[1]:
    return True
  else: 
    return False

