
def x_pronounce(sentence):
  from re import sub
  s = sub(r'\bx\b', 'ecks', sentence)
  s = sub(r'\bx', 'z', s)
  return sub(r'x', 'cks', s)

