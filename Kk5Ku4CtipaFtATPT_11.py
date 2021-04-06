
coconuts = ('coconuts', 'COCONUTS')
def coconut_translator(txt):
  res  = []
  for char in txt:
    bits = ord(char)
    res.append(''.join(coconuts[(bits >> (7-i)) & 0x1][i] for i in range(8)))
  return ' '.join(res)

