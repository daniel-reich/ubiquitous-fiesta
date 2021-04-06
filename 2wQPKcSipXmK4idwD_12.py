
def find_it(items, name):
​
  list_ = list(items.keys())
  
  for counter in range(len(list_)):
    if name == list_[counter]:
      return name[0].upper() + name[1:] + " is gone..."
  
  
  else:
    return name[0].upper() + name[1:] + " is here!"

