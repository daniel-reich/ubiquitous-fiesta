
def eratosthenes(num):
  if num <2: return []
  lst = []
  for n in range(2,num+1):
    if all(n%i for i in lst):
      lst+=[n]
  return lst

