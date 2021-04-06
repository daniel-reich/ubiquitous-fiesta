
def DECIMATOR(txt):
  m = len(txt)/10
  if m > int(m):
    m1 = int(m)+1
    return txt[:len(txt)-m1]
  else:
    return txt[:len(txt)-int(m)]

