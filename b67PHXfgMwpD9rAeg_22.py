
def plus_sign(txt):
  return len(txt) > 2 and all([txt[i+1]==txt[i-1]=="+" for i in range(len(txt)) if txt[i].isalpha()])

