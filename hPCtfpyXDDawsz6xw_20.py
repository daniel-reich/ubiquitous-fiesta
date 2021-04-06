
def verbify(txt):
  words = txt.split()
  if words[0].endswith("e"):
    words[0] +=  "d"
  elif not words[0].endswith("ed"):
    words[0] += "ed"
  return " ".join(words)

