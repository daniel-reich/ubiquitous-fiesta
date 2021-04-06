
def is_valid_hex_code(txt):
  a = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','a','b','c','d','e','f']
  s = 0
  
  for i in txt[1:]:
    if i in a:
      s = s
    else:
      s += 1
  
  if len(txt) > 7:
    s += 1
    
  if txt[0] != '#':
    s += 1
  
  return s == 0

