
def sort_contacts(names, sort):
  if not names: return []
  names.sort(key=lambda x : x.split()[1])
  return names if sort=="ASC" else names[::-1]

