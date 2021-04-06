
def is_central(txt):
  chrIdx = txt.index(txt.replace(" ", ""))
  return txt[:chrIdx].count(" ") == txt[chrIdx + 1:].count(" ")

