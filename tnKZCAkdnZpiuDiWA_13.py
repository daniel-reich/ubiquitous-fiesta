
def flip_end_chars(txt):
  if isinstance(txt, str)!=True:
    return "Incompatible."
  elif len(txt)<2:
    return "Incompatible."
  elif txt[0]==txt[-1]:
    return "Two's a pair."
  else:
    return txt[-1:]+txt[1:-1]+txt[0:1]

