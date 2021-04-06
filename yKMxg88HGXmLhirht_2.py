
def add_letters(l):
  r=chr(96+sum(ord(x)-96for x in l)%26)
  return ['z',r][r!='`']

