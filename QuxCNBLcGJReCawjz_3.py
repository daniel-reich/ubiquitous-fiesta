
def palindrome_type(n):
  d = str(n) == str(n)[::-1]
  b = bin(n)[2:] == bin(n)[:1:-1]
  answer = "Decimal and binary."
  if d and not b:
    answer = "Decimal only."
  elif b and not d:
    answer = "Binary only."
  elif not b and not d:
    answer = "Neither!"
  return answer

