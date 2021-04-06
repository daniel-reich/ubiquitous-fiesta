
def swap_dict(dic):
  new =  {}
  for key, value in dic.items(): 
    if value in new: 
      new[value].append(key) 
    else: 
      new[value]=[key] 
  return new

