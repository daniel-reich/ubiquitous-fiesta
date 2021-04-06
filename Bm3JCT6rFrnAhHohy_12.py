
def alphabet_index(txt):
  return ' '.join(str(ord(l)-96) for l in txt.lower() if l.isalpha())

