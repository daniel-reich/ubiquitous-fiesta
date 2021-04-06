
def organize(txt):
  if not txt:
    return {}
  info = ['name', 'age', 'occupation']
  types = [str, int, str]
  details = [func(item) for func, item in zip(types, txt.split(', '))]
  return {
    data_type: detail
    for detail, data_type in zip(details, info)
  }

