
def comments_correct(txt):
  return txt.count('/') % 2 == txt.count('*') % 2 == 0

