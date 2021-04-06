
def smith_type(number):
  
  digitalroot = digsum(number)
  digitalrootofSopf = digsum(sumofprim(number))
​
  if digitalroot != digitalrootofSopf:
    return "Not a Smith"
  elif isprime(number):
    return "Trivial Smith"
  elif (digsum(number+1) == digsum(sumofprim(number+1))) and not isprime(number + 1):
    return "Youngest Smith"
  elif (digsum(number-1) == digsum(sumofprim(number-1))) and not isprime(number - 1):
    return "Oldest Smith"
  else:
    return "Single Smith"
​
  
def digsum(num):
  dignum = num
  while len(str(dignum)) != 1:
    dignum = sum(int(dignum) for dignum in str(dignum))
  return dignum
​
def sumofprim(num):
  div = 0
  i = 2
  while i*i <=num:
    while (num % i) == 0:
      div += i
      num //= i
    i+=1
  if num > 1:
    div += num
  return div
​
def isprime(num):
  if num > 1: 
   for i in range(2, num//2): 
    if (num % i) == 0: 
      return False
      break
   else: 
      return True
  else:
    return False
print(smith_type(6))

