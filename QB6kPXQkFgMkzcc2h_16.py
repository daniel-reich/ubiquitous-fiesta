
def remove_abc(txt):
  if "a" in txt.lower() or "b" in txt.lower() or "c" in txt.lower():
    return txt.replace("a", "").replace("b", "").replace("c", "")
  else:
    return None

