
def inatorInator(inv):
​
  print(inv)
  print(inv[-1])
  print(inv[-1].lower())
  
  if inv[-1].lower() == 'a' or inv[-1].lower() == 'e' or inv[-1].lower() == 'i' or inv[-1].lower() == 'o' or inv[-1].lower() == 'u':
    new_inv = inv + '-inator '
    
  else:
    new_inv = inv + 'inator '
    
  return new_inv + str(len(inv)) + '000'

