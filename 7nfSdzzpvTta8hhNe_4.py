
def organize(txt):
  try: n,a,o = txt.split(',')
  except ValueError: return {}
  return {'name':n, 'age':int(a), 'occupation':o[1:]}

