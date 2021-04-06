
def sort_contacts(names, sort):
  if not names:
    return []
  y = sorted(names, key = lambda x: x.split(' ')[-1])
  if sort == 'DESC':
    return y[::-1]
  return y

