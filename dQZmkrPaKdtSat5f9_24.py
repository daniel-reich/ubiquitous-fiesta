
def single_occurrence(txt):
  if txt == "":
    return ""
  txt1 = txt.lower()
  for i in set(txt1):
    if txt1.count(i) ==1:     
      return i.upper()

