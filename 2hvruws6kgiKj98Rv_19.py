
def to_scottish_screaming(txt):
  return "".join(["e" if i in 'aeiou' else i for i in list(txt.lower())]).upper()

