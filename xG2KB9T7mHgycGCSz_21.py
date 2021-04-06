
def valid(txt):
  if txt == "":
    return False
  return len(txt) in [4, 6] and txt.isdigit()

