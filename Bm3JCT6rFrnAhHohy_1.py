
def alphabet_index(txt):
  return ' '.join(str(ord(i)-96) for i in txt.lower() if i.isalpha())

