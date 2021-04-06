
def atbash(txt):
  return "".join(chr(219-ord(x)) if x.islower() else chr(155-ord(x)) if x.isupper() else x for x in txt)

