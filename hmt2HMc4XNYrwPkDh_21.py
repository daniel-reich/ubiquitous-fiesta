
def invert(s):
  if len(s)==1:
    return s.swapcase()
  else:
    return s[::-1][0].swapcase()+invert(s[:-1])
  # your recursive solution here

