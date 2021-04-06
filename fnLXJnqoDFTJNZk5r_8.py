
def sort_contacts(names, sort):
  def split(name):
    return name.split()[1]
  if names == None or names ==[]:
    return []
  return sorted(names, key=split) if sort=='ASC' else sorted(names, key=split, reverse=True)

