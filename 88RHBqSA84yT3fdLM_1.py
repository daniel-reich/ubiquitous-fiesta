
def inator_inator(inv):
  original=inv
  if inv[-1] in 'ieuoaIEOUA':
    inv+="-"
  return inv+"inator {}000".format(len(original))

