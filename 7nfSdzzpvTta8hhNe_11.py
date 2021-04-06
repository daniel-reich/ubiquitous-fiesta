
def organize(txt):
  if txt:
    txt = txt.split(', ')
    return {'name':txt[0],'occupation':txt[2],'age':int(txt[1])}
  return {}

