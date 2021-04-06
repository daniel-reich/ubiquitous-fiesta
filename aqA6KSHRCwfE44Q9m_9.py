
def normalize(txt):
 if '.' in txt.lower():
  return txt.capitalize()
 elif '!' not in txt:
  return txt.capitalize()+'!'
 else:
  return txt.capitalize()

