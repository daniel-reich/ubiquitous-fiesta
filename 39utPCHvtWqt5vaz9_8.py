
def direction(lst):
  ttable = str.maketrans({
    'e': 'w', 'E': 'W', 'a': 'e', 'A': 'E'
  })
  
  nlst = []
  
  for item in lst:
    nlst.append(item.translate(ttable))
    
  return nlst

