
def palindrome_type(n):
  dec = eq(n)
  bi = eq(bin(n).replace("0b",""))
  
  if dec and bi:
    return "Decimal and binary."
  elif dec:
    return "Decimal only."
  elif bi:
    return "Binary only."
  else : return "Neither!"
  
def eq(a):
  return str(a) == str(a)[::-1]

