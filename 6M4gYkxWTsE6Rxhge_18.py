
def all_prime(lst):
  if(lst == []):
    return bool(0)
  else:
    for elem in lst:
      if(elem == 1):
        return bool(0)
      elif(elem > 3): 
        for i in range(2,(int(elem/2) + 2)):
          if(elem%i == 0):
            return bool(0)
    return bool(1)

