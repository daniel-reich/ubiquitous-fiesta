
def remove_abc(txt):
  if txt.find("a") == -1 and txt.find("b") == -1 and txt.find("c") == -1:
    return
  else:
    return txt.replace("a", "").replace("b", "").replace("c", "")

