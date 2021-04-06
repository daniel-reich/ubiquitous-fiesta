
def validate_spelling(txt):
  t = txt.replace(".","")
  t = t.replace("?","")
  t = t.replace("!","")
  return "".join(t.split()[0:len(t.split())-1]).upper() == t.split()[-1].upper()

