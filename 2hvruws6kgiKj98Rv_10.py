
def to_scottish_screaming(txt):
  return "".join("E" if c in "AIOU" else c for c in txt.upper())

