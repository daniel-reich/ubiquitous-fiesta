
def censor(s):
  txtl = s.split(' ')
  
  for i, val in enumerate(txtl):
    if len(val) > 4:
      txtl[i] = '*' * len(val)
      
  return ' '.join(txtl)

