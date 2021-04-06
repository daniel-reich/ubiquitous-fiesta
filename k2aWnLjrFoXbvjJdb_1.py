
def vigenere(text, keyword):
  al, code = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", text.isupper()
  text = [i for i in text.upper() if i.isalpha() and i]
  key = (keyword.upper() * 99)[:len(text)]
  return ''.join([al[(al.index(v)+(-al.index(key[i]) if code else al.index(key[i])))%26] for i,v in enumerate(text)])

