
def reverse_case(txt):
  return ''.join([i.upper() if i.islower() else i.lower() for i in txt])

