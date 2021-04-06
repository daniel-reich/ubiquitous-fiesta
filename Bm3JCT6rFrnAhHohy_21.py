
def alphabet_index(txt):
  txt = txt.lower()
  return ' '.join([str(ord(i) - 96) for i in txt if i.isalpha()])

