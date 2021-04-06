
def comments_correct(txt):
  while txt:
    if txt[0:2] == '//':
      txt = txt[2:]
    elif txt[0:4] == '/**/':
      txt = txt[4:]
    else:
      return False
  return True

