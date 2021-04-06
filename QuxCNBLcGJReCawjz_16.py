
def palindrome_type(n):
  d_p = str(n) == str(n)[::-1]
  b=bin(n)[2:]
  b_p = b == b[::-1]
  
  if d_p and b_p:
    return "Decimal and binary."
  elif d_p:
    return "Decimal only."
  elif b_p:
    return "Binary only."
  else:
    return "Neither!"

