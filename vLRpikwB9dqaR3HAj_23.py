
def is_ord_sub(sml, bigl):
  for e in sml:
    if e in bigl:
      bigl = bigl[bigl.index(e)+1:]
    else:
      return False
  return True

