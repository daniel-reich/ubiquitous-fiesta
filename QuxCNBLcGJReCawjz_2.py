
def palindrome_type(n):
  deci, bina = False, False
  if str(n) == str(n)[::-1]:
    deci = True
  if bin(n)[2:] == bin(n)[2:][::-1]:
    bina = True
  return 'Decimal and binary.' if deci and bina else 'Decimal only.' if deci else'Binary only.' if bina else"Neither!"

