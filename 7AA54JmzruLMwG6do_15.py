
def is_icecream_sandwich(txt):
  types = list(set(txt))
  
  if len(txt)>=3 and len(types)==2:
    ends = txt.split(types[1])
    
    if len(ends[0])==len(ends[-1]):
    
      return True
  
  return False

