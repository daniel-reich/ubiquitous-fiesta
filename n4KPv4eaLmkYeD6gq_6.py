
def face_interval(lst):
  if not isinstance(lst, list):
    return ':/'
  else:  
    m1 = min(lst)
    m2 = max(lst)
    diff = m2 - m1   
    return ''.join([':)' if i == diff else '' for i in lst]) or ':('

