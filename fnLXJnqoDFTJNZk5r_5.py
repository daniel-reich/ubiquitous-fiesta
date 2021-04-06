
def sort_contacts(names, sort):
  if not names:
    return []
  l2 = [Z.split() for Z in names]
  if sort == 'ASC':
    l3 = sorted(l2, key=lambda x: x[1])
  else:
    l3 = sorted(l2, key=lambda x: x[1], reverse=True)
  return [' '.join(Z) for Z in l3 ]

