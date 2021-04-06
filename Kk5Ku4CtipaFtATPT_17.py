
def coconut_translator(txt):
  return ' '.join(map(chr2co, txt))
    
def chr2co(c):
  co = 'coconuts'
  b = bin(ord(c)).replace('b', '')
  while len(b)< 8:
    b = '0' + b
  co_bin = zip(co, b)
  return ''.join([(c if i=='0' else c.upper()) for (c, i) in co_bin])

