
def atbash(txt):
  txt2='abcdefghijklmnopqrstuvwxyz'
  txt2='abcdefghijklmnopqrstuvwxyz'+txt2.upper()
  return ''.join([txt2[25 - txt2.index(i)] if i in txt2 else i for i in txt])

