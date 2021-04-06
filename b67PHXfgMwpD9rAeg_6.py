
def plus_sign(txt):
  ends = not txt[0].isalpha() and not txt[-1].isalpha()
  middle = all(txt[i-1]==txt[i+1]=="+" for i in range(1,len(txt)-1) if txt[i].isalpha())
  return ends and middle

