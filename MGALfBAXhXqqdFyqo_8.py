
def atbash(txt):
  return ''.join(chr(155-ord(i)) if i.isupper() else chr(219-ord(i)) if i.islower() else i for i in txt)

