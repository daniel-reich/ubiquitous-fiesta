
def is_icecream_sandwich(txt):
  if len(txt)<3 or len(set(txt))!=2: return False
  c=txt[0]
  while txt[0]==c:
    if txt[0]!=txt[-1]: return False
    txt=txt[1:-1]
  return len(set(txt))==1

