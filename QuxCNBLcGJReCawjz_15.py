
def palindrome_type(n):
  d=str(n)==str(n)[::-1]; b=bin(n)[2:]==bin(n)[:1:-1]
  if d and not b: return "Decimal only."
  if not d and b: return "Binary only."
  if d and b: return "Decimal and binary."
  return "Neither!"

