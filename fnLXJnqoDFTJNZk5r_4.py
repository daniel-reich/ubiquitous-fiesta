
def sort_contacts(names, sort):
  if names == None:
    return []
  names_sorted = sorted(names, key=lambda name: name.split(" ")[-1], reverse=sort == "DESC")
  return names_sorted

