
def is_valid(txt):
  return "YES" if len(txt)%len(set(txt))==0 or (len(txt)-1)%len(set(txt))==0 else "NO"

