
def flip_end_chars(txt):
  if type(txt) is not str or len(txt) < 2:
    return "Incompatible."
  if txt[0]==txt[-1]:
    return "Two's a pair."
  return txt[-1]+txt[1:-1]+txt[0]

