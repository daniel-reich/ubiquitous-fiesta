
def wave(txt):
  return [txt[:i].lower()+txt[i].upper()+txt[i+1:].lower() for i in range(len(txt)) if txt[i].isalpha()]

