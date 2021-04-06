
def palindrome_type(n):
  s = 1 if str(n)==str(n)[::-1] else 0
  b = 1 if bin(n)[2:]==bin(n)[2:][::-1] else 0
  if s and b: return 'Decimal and binary.'
  elif s: return 'Decimal only.'
  elif b: return 'Binary only.'
  else: return 'Neither!'

