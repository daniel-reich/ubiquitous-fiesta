
def is_boiling(temp):
  
  if temp.endswith('C'):
    return int(temp.strip('C')) >= 100
  if temp.endswith('F') :
    return int(temp.strip('F')) >= 212

