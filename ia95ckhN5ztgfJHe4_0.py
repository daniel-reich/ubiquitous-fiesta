
def comments_correct(txt):
  txt = txt.replace('/**/','')
  txt = txt.replace('//','')
  if len(txt) == 0:
    return True
  else:
    return False

