
def i_sqrt(n):
  return "invalid" if n < 0 else 0 if n<2 else i_sqrt(int(n**0.5))+1

