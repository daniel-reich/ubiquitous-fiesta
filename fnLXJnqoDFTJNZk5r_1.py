
def sort_contacts(names, sort):
  if not names: return []
  func = lambda x: x.split()[1]
  if sort == 'ASC':
    return sorted(names, key=func)
  return sorted(names, key=func, reverse=True)

