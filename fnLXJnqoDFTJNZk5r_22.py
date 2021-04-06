
def sort_contacts(names, sort):
  if not names:
    return []
  if sort == 'ASC':
    return sorted(names, key = lambda x: x.split()[1])
  return sorted(names, key = lambda x: x.split()[1], reverse = True)

