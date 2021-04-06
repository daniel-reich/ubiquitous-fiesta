
def prime(x):
  for i in [2,3,5,7]:
    if x not in [2,3,5,7] and x%i==0:
      return 0 
  return 1

