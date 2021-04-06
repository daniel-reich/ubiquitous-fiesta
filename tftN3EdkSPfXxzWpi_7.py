
def sentence_searcher(t, n):
  s, w = t.replace('. ', '.|').split('|'), t.split(' ')
  r = [i for i in range(len(w)) if '.' in w[i]]
  n = n + len(w) if n < 0 else n
  return s[r.index([i for i in r[::-1] if i >= n].pop())]

