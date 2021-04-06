
def grant_the_hint(txt):
  split = txt.split()
  maximum = max([len(x) for x in split])
  
  ret = []
  
  for i in range(0, maximum + 1):
    app = ""
    
    for word in split:
      tmp = ""
      for j, char in enumerate(word):
        if j < i:
          tmp += char
        else:
          tmp += '_'
      app += tmp + ' '
    
    ret.append(app[:len(app) - 1])
    
  return ret

