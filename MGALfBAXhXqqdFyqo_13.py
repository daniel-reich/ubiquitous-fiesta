
def atbash(txt):
  return "".join([chr(219-ord(i)) if i.islower() else chr(155-ord(i)) if i.isupper() else i for i in txt])

