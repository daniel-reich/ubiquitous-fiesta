
from re import sub
def keyboard_shortcut(s):
  c, s = 'Ctrl+C Ctrl+V', s.replace(' + ', '+')
  s = sub(r'(?<!(Ctrl\+C ))Ctrl\+V\s?', '', s)
  while c in s:
    s = s[:s.index(c)]*2 + s[s.index(c)+len(c)+1:]
  return s.rstrip().replace('Ctrl+C ', '')

