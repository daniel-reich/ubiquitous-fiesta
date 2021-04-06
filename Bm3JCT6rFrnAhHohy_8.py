
def alphabet_index(txt):
  b = []
  a = ''
  c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for x in txt.lower():
    if x in c:
      a = a + x
  for i in a:
    b.append(str(ord(i) - 96))
  return ' '.join(b)

