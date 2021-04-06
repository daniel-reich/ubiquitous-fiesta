
def truncate(txt, length):
  if length > len(txt):
    return txt
  elif txt[length] == ' ':
    return txt[:length]
  else:
    txt = txt[:length]
    if ' ' not in txt:
      return ''
    return txt[:txt.rfind(' ')]

