
def plus_sign(txt):
  if txt[0]==txt[-1]=='+':
    return all(txt[i-1]==txt[i+1]=='+' for i in range(len(txt)) if txt[i].isalpha())
  return False

