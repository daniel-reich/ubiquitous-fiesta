
def sort_contacts(names, sort):
  if names==[] or names==None:
    return []
  new=[name.split(' ')[::-1] for name in names]
  new=[' '.join(i) for i in new]
  if sort=='ASC':
    new=sorted(new)
  else:
    new=sorted(new,reverse=True)
  new=[c.split(' ')[::-1] for c in new]
  new=[' '.join(i) for i in new]
  return new

