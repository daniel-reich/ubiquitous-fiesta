
def sort_contacts(names, sort):
  if names and names!=[]:
      names.sort(key=lambda x:x.split()[1],reverse=sort=='DESC')
      return names
  return []

