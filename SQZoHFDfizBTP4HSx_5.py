
def missing_alphabets(txt):
  a = 'abcdefghijklmnopqrstuvwxyz'
  mx = max([txt.count(i) for i in txt])
  return ''.join([i*(mx-txt.count(i)) for i in a])

