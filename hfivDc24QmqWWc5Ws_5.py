
def eratosthenes(num):
  #remove all bad inputs
  if num < 2:
    return []
​
  primeList = []
  i = 2
  while i < num:
  
    #figure out if i is prime
    isPrime = True
​
    for x in range(2, i):
      if i % x == 0:
        isPrime = False
    
    #if it's prime, append it to list
    if isPrime:
      primeList.append(i)
      
      
    i += 1
    
  return primeList

