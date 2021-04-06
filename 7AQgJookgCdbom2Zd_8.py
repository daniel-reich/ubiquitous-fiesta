
def pig_latin(txt):
  tlst = txt.split()
  for i,w in enumerate(tlst):
    up = w[0].isupper()
    w = w.lower()
    punc = w[-1] if not w[-1].isalpha() else ''
    w = w[:-1] if punc else w
    if w[0] in 'aeiou':
      w += 'way'
    else:
      w = w[1:]+w[0]+'ay'
    tlst[i] = (w+punc).capitalize() if up else w+punc
  return ' '.join(tlst)

