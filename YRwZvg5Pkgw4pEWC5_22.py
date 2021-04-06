
def flick_switch(lst):
  if not lst: return []
  a = [True if lst[0]!="flick" else False]
  b = lst[1:]
  while b:
      if b[0]=="flick":
          a.append(not a[-1])
      else:
          a.append(a[-1])
      b.pop(0)
  return a

