
def plus_sign(txt):
  if len(txt)<3: return False
  for i in range(1,len(txt)-1):
    if txt[i].isalpha():
      if txt[i-1] != '+' or txt[i+1] != '+':
        return False
  return True

