
def high_low(txt):
  txt = txt.split(" ")
  a = max(txt,key=int)
  b = min(txt)
  return a+' '+b

