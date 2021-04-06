
def reverse(txt):
  ret = []
  
  for i in txt.split(" "):
    
    if len(i) >= 5:
      ret.append(i[::-1])
    else:
      ret.append(i)
  
  return ' '.join(i for i in ret)

