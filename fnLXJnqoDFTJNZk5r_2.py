
def sort_contacts(names, sort):
  if not isinstance(names, list):
    return []
  value = lambda name: name.split()[1]
  return sorted(names, key = value, reverse = (sort == 'DESC'))

