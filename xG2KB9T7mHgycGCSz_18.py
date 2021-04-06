
def valid(txt):
  if len(txt)>0 and len(txt)==4 or len(txt)==6:
    return len([x for x in txt if x.isnumeric()])==len(txt)
  return False

