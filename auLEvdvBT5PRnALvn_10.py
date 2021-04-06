
def mirror_cipher(m,key="abcdefghijklmnopqrstuvwxyz"):
  return ''.join(key[::-1][key.index(i)] if i in key else i for i in m.lower())

