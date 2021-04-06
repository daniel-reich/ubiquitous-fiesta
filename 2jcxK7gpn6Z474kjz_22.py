
def security(t):
  q = t.replace('x','')
  if 'T$' in q or '$T' in q:
    return 'ALARM!'
  return 'Safe'

