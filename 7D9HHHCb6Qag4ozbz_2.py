
def find_zip(txt):
  if txt.count('zip') < 2:
    return -1
  else:
    return txt.rfind("zip")

