
def plus_sign(txt):
  ref = txt.split('+')
  ch = all([i[:len(i)//2 +1]==i[len(i)//2:][::-1] for i in ref[1:-1]])
  if ref[0]=='':return ch
  return False

