
def plus_sign(txt):
  return not (txt[0].isalpha() or txt[-1].isalpha()) and all(txt[i-1]+
    txt[i+1]=="++" for i in range(len(txt)) if txt[i].isalpha())

