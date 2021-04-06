
def normalize(txt):
  if txt.isupper()==True:
    return txt.lower().capitalize()+"!"
  else:
    return txt

