
def flip_end_chars(txt):
  if not isinstance(txt , str):
    return "Incompatible."
  if len(txt)<1:
    return "Incompatible."
  if txt[0]==txt[-1]:
    return "Two's a pair."
  return txt[-1]+txt[1:-1]+txt[0]

