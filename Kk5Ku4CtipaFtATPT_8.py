
def coconut_translator(txt):
  A=[bin(ord(x))[2:].zfill(8) for x in txt]
  k='coconuts'
  B=[''.join([k[i].upper() if x[i]=='1' else k[i] for i in range(8)]) for x in A]
  return ' '.join(B)

