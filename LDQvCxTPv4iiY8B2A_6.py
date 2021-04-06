
def same_upsidedown(ntxt):
  a=''
  for e in str(ntxt):
    if e=='9':
      a='6'+a
    elif e=='6':
      a='9'+a
    else:
      a=e+a
  return a==str(ntxt)

