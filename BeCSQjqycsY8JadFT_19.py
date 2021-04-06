
def recur_index(txt,idx=0):
  if txt==None or len(txt)<2:return {}
  if txt[0] in txt[1:]:
    pos=txt[1:].index(txt[0])+1
    tmp=recur_index(txt[1:pos],idx+1)
    if tmp!={}:return tmp
    return {txt[0]:[idx,idx+pos]}
  if len(txt)>1:return recur_index(txt[1:],idx+1)
  return {}

