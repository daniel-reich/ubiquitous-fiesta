
def isPrime(number):
  isAPrimeNumber = False
  for i in range(2, number):  
      if (number % i) == 0:  
          isAPrimeNumber = False 
          break
      else:  
          isAPrimeNumber = True
  return isAPrimeNumber
def moran(number):
  numberStr = str(number)
  sumOfDigits = 0
  for i in numberStr:
      sumOfDigits += int(i)
  if number % sumOfDigits == 0:
      if isPrime(int(number/sumOfDigits)) == True:
          return "M"
      else:
          return "H"
  else:
      return "Neither"

