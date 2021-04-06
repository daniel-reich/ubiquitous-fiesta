
def is_valid_hex_code(txt):
  ch='#'
  print(txt[0])
  if len(txt)!=7:
    print("her1")
    return False
  if txt[0]!=ch:
    
    return False
  l=['a','b','c','d','e','f','A','B','C','D','E','F']
  print(txt)
  for i in txt[1:]:
    print(i)
    if (i in l) or i.isdigit():
      
      pass
    else:
    
      return False
  return True

