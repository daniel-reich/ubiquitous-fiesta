
def is_valid_hex_code(txt):
  s=['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','A','B','C','D','E','F']
  if(len(txt)!=7):  
    return False
  for i in range(1,7):
    if(txt[i]not in s):
      return False
  return True

