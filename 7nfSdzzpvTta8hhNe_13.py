
def organize(txt):
  if txt:
    n, a, o = txt.split(', ')
    return {'name': n, 'occupation': o, 'age': int(a)} 
  return {}

