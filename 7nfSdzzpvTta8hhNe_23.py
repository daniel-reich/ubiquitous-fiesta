
def organize(txt):
  if not txt: return {}
  txt = txt.split(', ')
  return {'name': txt[0], 'age': int(txt[1]), 'occupation': txt[2]}

