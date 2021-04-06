
def seven_segment(txt):
  lst = []
  for i in range(1,len(txt)):
    lst.append(change(txt[i-1],txt[i]))
  return lst
  
def change(a,b):
  d = {'0':'abcdef','1':'bc','2':'abdeg','3':'abcdg','4':'bcfg','5':'acdfg','6':'acdefg','7':'abc','8':'abcdefg','9':'abcfg'}
  a,b = d[a], d[b]
  lst = []
  for i in a:
    if i not in b:
      lst.append(i)
  for i in b:
    if i not in a:
      lst.append(i.upper())
  return sorted(lst,key=lambda x:x.lower())

