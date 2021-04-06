
def isprime(n):
  prime = True
  if n>1:
    for i in range(2, n):
      if n%i == 0:
        prime = False
        break
  else:
    prime = False
  return prime
​
def truncatable(n):
  # left truncatable prime
  left = True
  for i in range(len(str(n))):
      if not isprime(int(str(n)[i:])):
          left = False
          break
          
  #right truncatable prime
  right = True
  for i in range(len(str(n))):
      if not isprime(int(str(n)[0:len(str(n))-i])):
          right = False
          break
          
  if "0" in str(n):
    right = False
    left = False
  
  if right == True and left == False:
    return "right"
  if right == False and left == True:
    return "left"
  if right == True and left == True:
    return "both"
  if right == False and left == False:
    return False

