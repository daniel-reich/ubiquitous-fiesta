
def security(txt):
  simp = ''.join(l for l in txt if l!='x')
  return 'ALARM!' if 'T$' in simp or '$T' in simp else 'Safe'

