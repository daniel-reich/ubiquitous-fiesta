
def palindrome_type(n):
  if str(n) == str(n)[::-1]:
    if str(bin(n)[2:]) == str(bin(n)[2:])[::-1]:
      return 'Decimal and binary.'
    else:
      return 'Decimal only.'
  else:
    if str(bin(n)[2:]) == str(bin(n)[2:])[::-1]:
      return 'Binary only.'
    else:
      return 'Neither!'

