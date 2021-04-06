
def alphabet_index(txt):
  return ' '.join(map(str, (ord(c)-ord('a')+1 for c in txt.lower() if 'a' <= c <= 'z')))

