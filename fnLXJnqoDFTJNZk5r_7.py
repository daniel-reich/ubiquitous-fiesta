
def sort_contacts(names, sort):
  f={}
  if names :
    for i in range(len(names)):
      a,b = names[i].split(" ")
      f[b]=names[i]
    if sort == "ASC":
      sorted_dict =sorted(f.keys())
    if sort == "DESC":
      sorted_dict = sorted(f.keys(), reverse=True)
    return [f[i] for i in sorted_dict]
  else:
    return []

