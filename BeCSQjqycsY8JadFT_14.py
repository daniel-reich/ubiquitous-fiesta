
def recur_index(txt, prev=None):
  if prev is None: prev = {}
  if not txt: return {}
  if txt[0] in prev: return {txt[0]:[prev[txt[0]],len(prev)]}
  prev[txt[0]] = len(prev)
  return recur_index(txt[1:], prev)

