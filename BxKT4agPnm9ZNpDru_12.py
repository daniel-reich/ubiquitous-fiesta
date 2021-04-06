
def zip_it(women, men): 
  set1 = tuple(women)
  set2 = tuple(men)
  
  if len(women) == len(men):
    return list(zip(set1, set2))
  else:
    return "sizes don't match"

