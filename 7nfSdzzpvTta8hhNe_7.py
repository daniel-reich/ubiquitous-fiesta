
def organize(txt):
  if txt: 
    obj = txt.split(',')
    return  dict({'name':obj[0], 'age':int(obj[1]), 'occupation':obj[2].strip(' ')})
  return {}

