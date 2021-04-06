
def neutralise(s1, s2):
  str = ''
  for i in range(len(s2)):
    if  s1[i] == s2[i]: str += s1[i]
    else: str += '0'
  return str

