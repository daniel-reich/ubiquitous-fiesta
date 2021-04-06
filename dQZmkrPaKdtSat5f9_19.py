
def single_occurrence(txt):
  if txt == "":
    return ""
  else:
    for i in txt:
      if txt.count(i.lower()) + txt.count(i.upper()) == 1:
        return i.upper()

