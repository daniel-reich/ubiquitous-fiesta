
def recur_index(t,a=''):
  if not t: return {}
  if t[0] in a: return {t[0]: [a.find(t[0]),len(a)]}
  else: return recur_index(t[1:],a+t[0])

