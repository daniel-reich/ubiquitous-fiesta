
def sort_contacts(lst, sort):
  if lst == None: return []
  if sort == "ASC": return sorted(lst,key= lambda x: x.split()[1])
  return sorted(lst,key= lambda x: x.split()[1],reverse=True)

