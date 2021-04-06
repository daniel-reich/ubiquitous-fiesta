
def recur_index(txt,i=0):
  if not txt or i==len(txt):
    return {}
  if txt.index(txt[i])<i:
    return {txt[i]:[txt.index(txt[i]),i]}
  return recur_index(txt,i+1)

