
def same_upsidedown(ntxt):
  return ntxt == ntxt.translate(str.maketrans("69","96"))[::-1]

