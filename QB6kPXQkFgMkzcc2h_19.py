
def remove_abc(txt):
  new = ""
  if "a" not in txt and "b" not in txt and "c" not in txt:
    return None
  else:
    for char in txt:
      if char != "a" and char != "b" and char != "c":
        new += char
  return new

