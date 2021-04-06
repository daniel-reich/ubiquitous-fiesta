
def wave(txt):
  return [txt[:i] +txt[i].upper()+txt[i+1:] for i in range(len(txt)) if txt[i] != " "]

