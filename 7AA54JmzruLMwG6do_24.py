
def is_icecream_sandwich(txt):
  if len(txt)<3: return False
  ends = [x for x in txt.split(txt[(len(txt)-1)//2]) if x]
  return len(set(ends))==1 and len(ends)==2

