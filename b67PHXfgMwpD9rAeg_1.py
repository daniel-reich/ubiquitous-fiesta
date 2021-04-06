
def plus_sign(txt):
  txt = ' ' + txt + ' '
  letters = sum(i.isalpha() for i in txt)
  signed = sum(i.isalpha() for i in txt.split('+'))
  return letters == signed

