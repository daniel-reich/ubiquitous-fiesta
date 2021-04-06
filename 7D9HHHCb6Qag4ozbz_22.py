
def find_zip(txt):
  return txt.rfind('zip', 2) if txt.count('zip') > 1 else -1

