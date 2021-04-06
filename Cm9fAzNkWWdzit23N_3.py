
def wave(txt):
  return [txt[:i]+str.upper(txt[i])+ txt[i+1:] for i in range(len(txt)) if txt[i].isalpha()]

