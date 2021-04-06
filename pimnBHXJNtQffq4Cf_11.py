
def mapping(letters):
  print(type(letters), letters)
  
  new_dict = {}
  for item in letters:
    new_dict[item] = item.upper()
    
  return new_dict

