
def sort_contacts(names, sort):
  try:
    status = {'DESC': True, 'ASC': False}
    return sorted(names, key = lambda x: x.split()[1], reverse = status[sort])
  except TypeError:
    return []

