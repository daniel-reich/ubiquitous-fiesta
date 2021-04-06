
def sort_contacts(names, sort):
  if names:
    L=[x.split() for x in names]
    L.sort(key=lambda x: x[1])
    if sort=="ASC":
      return [' '.join(x) for x in L]
    else:
      return [' '.join(x) for x in L[::-1]]
  else:
    return []

