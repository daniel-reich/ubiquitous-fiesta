
def truncate(txt, length):
  if len(txt) <= length:
    return txt
  elif txt[length] == " ":
    return txt[:length]
  else:
    pos = txt[:length].rfind(" ")
    if pos < 0:
      return ""
    else:
      return txt[:pos]

