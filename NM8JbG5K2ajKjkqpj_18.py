
def asc_des_none(lst, s):
  if s=="Asc":
    return sorted(lst)  
  elif s=='Des':
    return list(reversed(sorted(lst)))
  else:
    return lst

