
def sort_contacts(names, sort):
  if not names: names = []
  return sorted(names, key=lambda x: x.split()[1])[::[1, -1][sort == 'DESC']]

