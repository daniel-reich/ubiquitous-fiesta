
def mumbling(s):
  return '-'.join(s[i].upper() + s[i].lower()*i for i in range(len(s)))

