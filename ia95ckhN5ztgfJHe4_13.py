
def comments_correct(txt):
  txt = txt.replace("/**/", '')
  txt = txt.replace("//", '')
  return True if txt=='' else False

