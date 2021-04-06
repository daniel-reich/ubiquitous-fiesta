
def find_longest(s,l=''):
  s = ''.join([i.lower() if i.isalpha() else ' ' for i in s]).split()
  if not len(s):
    return l
  return find_longest(' '.join(s[1:]),s[0]) if len(s[0])>len(l) else find_longest(' '.join(s[1:]),l)

