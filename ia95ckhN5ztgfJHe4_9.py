
def comments_correct(txt):
  while len(txt) > 1:
    if txt[:4] == "/**/":
      txt = txt[4:]
    elif txt[:2] == "//":
      txt = txt[2:]
    else:
      break
  return not len(txt) > 0

