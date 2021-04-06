
def palindrome_type(n):
      if str(n)==str(n)[::-1]:
            if bin(n)[2::]==bin(n)[:1:-1]: return "Decimal and binary."
            else: return "Decimal only."
      if bin(n)[2::]==bin(n)[:1:-1]: return "Binary only."
      return "Neither!"

