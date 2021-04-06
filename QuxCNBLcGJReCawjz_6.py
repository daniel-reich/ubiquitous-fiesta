
def palindrome_type(n):
  b = bin(n)[2:]
  res = [(1 if str(n)==str(n)[::-1] else 0), (1 if b==b[::-1] else 0)]
  return "Decimal and binary." if res==[1,1] else "Decimal only." if res==[1,0] else "Binary only." if res==[0,1] else "Neither!"

