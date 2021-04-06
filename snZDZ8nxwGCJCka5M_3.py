
def pyramidal_string(txt, _type):
​
  if not is_triangular(len(txt)): return 'Error!'
    
  pyramid = []
  lst = list(txt)
  i = 1
  
  while lst:
    level = []
    
    while len(level) < i:
      if _type == 'REG': level.append(lst.pop(0))
      if _type == 'REV': level.insert(0, lst.pop())
    
    if _type == 'REG': pyramid.append(' '.join(level))
    if _type == 'REV': pyramid.insert(0, ' '.join(level))
    i += 1
      
  return pyramid
    
  
def is_triangular(n): 
  return not (8*n+1)**0.5 % 1

