
def direction(lst):
​
  d = {'e': 'w','E':'W','a':'e','A':'E','s':'s','S':'S','t':'t',
  'T':'T',' ':' '}
  out = []
  for e in lst:
    w = ''
    for l in e:
      w+=d[l]
    out.append(w)
  return out

