
def flip_end_chars(txt):
  if len(txt) >= 2 and type(txt) is not list and txt[0] != txt[-1]:
    return txt[-1]+txt[1:-1]+txt[0]
  elif type(txt) is list or txt == "":
    return "Incompatible."
  elif txt[0] == txt[-1]:
    return "Two's a pair."

