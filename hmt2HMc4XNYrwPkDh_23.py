
def invert(s):
  letter = s[-1].swapcase()
​
  if len(s) > 1:
      return letter + invert(s[:-1:])
​
  else:
      return letter

