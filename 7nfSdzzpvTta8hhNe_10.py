
def organize(txt):
  if len(txt) == 0:
    return {}
  else:
    return {'name': txt.split(',')[0],'age': int(txt.split(',')[1]), 'occupation': txt.split(',')[2].lstrip()}

