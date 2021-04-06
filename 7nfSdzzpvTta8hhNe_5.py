
def organize(txt):
  if txt: a,b,c = txt.split(',') 
  return {'name': a, 'age': int(b[1:]), 'occupation': c[1:]} if txt else {}

