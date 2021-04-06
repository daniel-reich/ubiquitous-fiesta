
def flip_end_chars(txt):
  try:
    if len(txt) < 2:
      return "Incompatible."
    elif txt[0] == txt[len(txt)-1]:
      return "Two's a pair."
    else:
      first = txt[0]
      last = txt[len(txt)-1]
      return last + txt[1:len(txt)-1] + first
  except TypeError:
    return "Incompatible."

