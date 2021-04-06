
def remove_abc(txt):
  if "a" not in txt and "b" not in txt and "c" not in txt:
    return None
  else:
    return txt.replace("a", "").replace("b","").replace("c","")

