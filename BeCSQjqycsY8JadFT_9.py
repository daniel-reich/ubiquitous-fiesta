
def recur_index(s, d=None, i=0):
  if d is None: d = dict()
  if not s: return {}
  if s[0] in d: return {s[0]: d[s[0]]+[i]}
  d[s[0]] = [i]
  return recur_index(s[1:], d, i+1)

