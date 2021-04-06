
def validate_relationships(txt):
  txt = txt.replace("=","==")
  if "<==" in txt:
    txt = txt.replace("<==", "<=")
  if ">==" in txt:
    txt = txt.replace(">==", ">=")
  return eval(txt)

