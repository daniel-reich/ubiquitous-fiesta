
def is_icecream_sandwich(txt):
  if len(txt)>2 and txt==txt[::-1] and len(set(txt))==2:
    return True
  return False

