
def missing_letter(txt):
  s = ''
  for x in range(ord(txt[0]), ord(txt[-1])):
    if chr(x) not in txt:
      s+= chr(x)
      return s
  return "No Missing Letter"

