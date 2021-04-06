
def recur_index(txt):
  def recurssion(txt, index, indexes = {}):
    
    
    if txt == None:
      return {}
    if index == len(txt)-1 or len(txt) == 0 :
      return {}
    l8r = txt[index]
    if l8r in indexes.keys():
      return {l8r: [indexes[l8r], index]}
    else:
      indexes[l8r] = index
      #print(txt, index, l8r, indexes)
      return recurssion(txt, index+1, indexes)
  if txt == None:
    return {}
  r = recurssion(txt, 0)
  return r

