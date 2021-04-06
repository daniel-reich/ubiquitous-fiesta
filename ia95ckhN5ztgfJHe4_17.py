
def comments_correct(txt):
  if len(txt) % 2 == 1:
    return False
  elif txt.count("/") == len(txt) and len(txt) % 2 == 0:
    return True
  elif "/*/" in txt:
    return False
  else:
    return True

