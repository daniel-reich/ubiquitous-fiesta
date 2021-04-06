
def coconut_translator(txt):
  translation = []
  for i in txt:
    byte, word = bin(ord(i))[2:].zfill(8), ''
    
    for a, b in zip('coconuts', byte):
      if b == '1':
        word += a.upper()
      else:
        word += a
    translation.append(word)
    
  return ' '.join(translation)

