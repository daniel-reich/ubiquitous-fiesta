
def palindrome_type(n):
  d = list(str(n))
  d.reverse()
  b = list(bin(n))[2:]
  b.reverse()
​
  if list(str(n)) == d and list(bin(n))[2:] == b:
    return "Decimal and binary."
  
  if list(str(n)) == d:
    return "Decimal only."
  
  if list(bin(n))[2:] == b:
    return "Binary only."
    
  return "Neither!"

