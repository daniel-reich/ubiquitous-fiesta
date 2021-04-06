
def find_longest(s, wi = 0, max_size = 0, largest = None):
  
  if isinstance(s, str) == True:
    s = s.replace('.', '').replace('\"', '')
    s = s.split()
  
  if wi == len(s):
    return largest.lower()
  else:
    if len(s[wi]) > max_size:
      if '\'' in s[wi]:
        s[wi] = s[wi].split('\'')[0]
      max_size = len(s[wi])
      largest = s[wi]
    return find_longest(s, wi+1, max_size, largest)

