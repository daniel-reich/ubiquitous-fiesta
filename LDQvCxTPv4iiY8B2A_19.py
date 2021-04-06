
def same_upsidedown(txt):
  flipped_txt = txt.translate(str.maketrans('69', '96'))[::-1]
  return flipped_txt == txt

