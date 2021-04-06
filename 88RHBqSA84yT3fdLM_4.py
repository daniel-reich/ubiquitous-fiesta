
def inatorInator(inv):
  strLen = len(inv)
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  if inv[-1] in vowels:
    inv=inv+"-"
  inv=inv+"inator "+str(strLen)+"000"
  return inv

