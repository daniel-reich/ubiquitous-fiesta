
def reverse_case(txt):
  return "".join([x.lower() if x==x.upper() else x.upper() for x in txt])

