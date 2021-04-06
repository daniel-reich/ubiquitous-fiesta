
def palindrome_type(n):
  decimal = str(n) == str(n)[::-1]
  binary = bin(n)[2:] == bin(n)[2:][::-1]
  if decimal and binary:
    return 'Decimal and binary.'
  elif decimal:
    return 'Decimal only.'
  elif binary:
    return 'Binary only.'
  else:
    return 'Neither!'

