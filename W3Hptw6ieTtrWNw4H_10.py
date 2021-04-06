
def bifid(text):
  a = 'abcdefghiklmnopqrstuvwxyz'
  b = iter(a)
  d1 = {next(b):(r,c) for r in range(1,6) for c in range(1,6)}
  d2 = {v:k for k,v in d1.items()}
  enc = True if ' ' in text else False
  t = str.maketrans('j', 'i')
  text = ''.join(c for c in text.lower().translate(t) if c in a)
  if enc:
    tmp = [d1[c][0] for c in text] + [d1[c][1] for c in text]
    tups = [(tmp[i], tmp[i+1]) for i in range(0, len(tmp), 2)]
  else:
    tmp = [n for c in text for n in d1[c]]
    l2 = len(tmp) // 2
    tups = zip(tmp[:l2], tmp[l2:])
  return  ''.join([d2[tup] for tup in tups])

