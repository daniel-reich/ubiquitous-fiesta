
def sort_contacts(names, sort):
  return [] if names==None else sorted(names,key=lambda x:x.split()[1], reverse=True if sort=="DESC" else False)

