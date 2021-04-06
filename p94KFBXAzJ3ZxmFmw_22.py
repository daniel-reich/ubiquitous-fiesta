
def ascii_capitalize(txt):
  return "".join([i.upper()if not ord(i)%2 else i.lower()for i in txt])

