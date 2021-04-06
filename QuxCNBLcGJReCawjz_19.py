
def palindrome_type(n):
  binary = bin(n)[2:]
  if str(n)==str(n)[::-1]:
    if binary == binary[::-1]:
      return "Decimal and binary."
    return "Decimal only."
  if binary == binary[::-1]:
    return "Binary only."
  return "Neither!"

