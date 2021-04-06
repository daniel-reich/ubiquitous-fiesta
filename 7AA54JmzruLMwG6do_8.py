
def is_icecream_sandwich(txt):
  return txt==txt[::-1] and len(set(txt))==2

