
def compress(chars):
  def splitter(chars):
    nl = []
    l = []
    
    for char in chars:
      if l == []:
        l.append(char)
      elif l[0] == char:
        l.append(char)
      else:
        nl.append(l)
        l = [char]
    
    if l != []:
      nl.append(l)
    
    return nl
  string = lambda lst: lst[0] if len(lst) == 1 else lst[0] + str(len(lst))
  
  s = splitter(chars)
  
  return ''.join([string(s[n]) for n in range(len(s))])

