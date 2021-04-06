
def is_icecream_sandwich(txt):
 if len(txt) < 3: return False
 top = ''
 for i in txt:
  if i == txt[0]: top += i
  else: break
 t = len(top)
 ics = [txt[:t], txt[t:-t], txt[-t:]]
 return all([ics[0]==ics[2],len(set(ics[1]))==1,ics[1]!=''])

