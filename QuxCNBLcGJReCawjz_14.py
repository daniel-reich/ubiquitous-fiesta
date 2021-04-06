
def is_valid(str):
  for i in range(len(str) // 2):
    if str[i] != str[-1 - i]:
      return False
  return True
​
def palindrome_type(n):
  f1, f2 = is_valid(str(n)), is_valid(bin(n)[2:])
  if f1 and f2:
    return "Decimal and binary."
  elif f1:
    return "Decimal only."
  elif f2:
    return "Binary only."
  else:
    return 'Neither!'

