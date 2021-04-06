
def alph_num(txt):
  return ' '.join(str(ord(i) - ord('A')) for i in txt)

