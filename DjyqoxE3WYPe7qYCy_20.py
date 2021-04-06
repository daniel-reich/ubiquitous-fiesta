
def reverse_odd(txt):
  txt = txt.split(' ')
  txt = [i[::-1] if len(i) % 2 != 0 else i for i in txt]
  return ' '.join(txt)

