
def no_yelling(phrase):
  import re
  x = re.sub(r'(^[?!])\1+',r"\1",phrase[::-1])
  return x[::-1]

