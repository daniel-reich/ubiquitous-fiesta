
def comments_correct(txt):
  txt = txt.replace("/**/","")
  txt = txt.replace("//", "")
  return len(txt) == 0

