
def keyboard_mistakes(txt):
  w = 'OI  AS'
  return ''.join(w[int(i)] if i.isdigit() else i for i in txt)

