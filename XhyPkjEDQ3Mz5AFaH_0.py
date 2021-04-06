
def is_match(s,p):
  if s==p=="": return True
  if p=="": return False
  if p[-1]!="*": return is_match(s[:-1],p[:-1])
  if p[-2]==".": return True
  r = s.index(p[-2])
  return is_match(s[:r],p[:-2])

