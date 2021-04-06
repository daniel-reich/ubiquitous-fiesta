
def find_zip(txt):
  if(txt.count("zip", 0, 200) > 1):
    return txt.rfind("zip")
  else:
    return -1

