
def pad(txt):
  if len(txt)!= 140 and not len(txt)%2: txt+= " "
  while len(txt)< 140: 
    txt+="lo"
  if len(txt)>140: return txt[:-1]
  return txt

