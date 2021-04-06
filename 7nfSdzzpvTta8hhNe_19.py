
def organize(txt):
  if not txt: return {}
  items = txt.split(', ')
  return {'name':items[0], 'age': int(items[1]), 'occupation': items[2]}

