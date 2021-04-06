
def ink_levels(inks):
  minimum = None
  for item in inks: 
    if minimum == None:
      minimum = inks[item]
    elif inks[item] < minimum:
      minimum = inks[item]
  
  
  return minimum

