
def find_longest(s,m=''):
  if not m:
    s = s.lower().split()
  try:
    m = s[0]
    if m.endswith("'s"):
      m = m[:-2]
    if not m.isalpha():
      m = ''.join(i for i in m if i.isalpha())
    return max((m, find_longest(s[1:], m)), key=len)
  except:
    return ''

