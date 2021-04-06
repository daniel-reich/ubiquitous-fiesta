
def flip_end_chars(txt):
  if isinstance(txt,str):
    if len(txt)>=2:
      if txt[0]==txt[-1]:
        return "Two's a pair."
      else:
        return txt[-1]+txt[1:-1]+txt[0]
    else:
      return "Incompatible."
  else:
    return "Incompatible."

