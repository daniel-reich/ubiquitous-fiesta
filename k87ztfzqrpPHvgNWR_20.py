
def widen_streets(lst, n):
  lst = [l.replace("#   #","# l #") if i==0 else l for i,l in enumerate(lst)]
  lst = [x.replace(" "," "*n) for x in lst]
  lst = [l.replace("l"," ") if i==0 else l for i,l in enumerate(lst)]
  return lst

