
def find_zip(txt):
  if txt.count("zip") > 1:
    return txt.rindex("zip")
  else:
    return -1

