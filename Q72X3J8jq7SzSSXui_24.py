
def sentence_searcher(s, w):
  s = s.replace('. ', '.|').split('|')
  for t in s:
    if w.lower() in t.lower(): return t
  return ''

