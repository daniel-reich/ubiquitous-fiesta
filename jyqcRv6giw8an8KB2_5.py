
def invert(s):
  return "".join([i.lower() if i.isupper() else i.upper() for i in s ][::-1])

