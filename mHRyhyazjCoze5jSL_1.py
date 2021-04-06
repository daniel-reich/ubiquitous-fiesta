
def double_swap(txt, c1, c2):
  dct = {c1:c2,c2:c1}
  return ''.join(dct[x] if x in dct else x for x in txt)

