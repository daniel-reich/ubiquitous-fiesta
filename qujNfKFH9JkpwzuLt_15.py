
def first_index(h,w):
  s=''.join(bytearray.fromhex(i).decode()if 20<int(i,16)<127else' 'for i in h.split())
  return s.index(w)

