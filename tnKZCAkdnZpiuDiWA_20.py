
def flip_end_chars(txt):
  if (type(txt) != str or len(txt) <= 1):
    return "Incompatible."
  elif txt[0] == txt[-1]:
    return "Two's a pair."
  else:
    return txt[-1]+txt[1:-1]+txt[0]

