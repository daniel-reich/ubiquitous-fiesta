
def magic(txt):
  m, d, y = txt.split(' ')
  if int(m)*int(d) == int(y[-1]):
    return True
  elif int(m)*int(d) == int(y[-2:]):
    return True
  elif int(m)*int(d) == int(y[-3:]):
    return True
  else:
    return False

