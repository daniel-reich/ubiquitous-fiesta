
def flick_switch(lst):
  a=True
  c=[]
  for i in range(len(lst)):
    if lst[i]!="flick":
      c.append(a)
    if lst[i]=="flick":
      a=not a
      c.append(a)
    
  return c

