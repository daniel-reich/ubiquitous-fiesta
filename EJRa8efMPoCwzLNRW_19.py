
def pos(w):
  for l in w:
    if l.isdecimal():
      return int(l)
​
​
def no_num(w):
  return ''.join(l for l in w if not l.isdecimal())
​
​
def dakiti(sentence):
  sentence = sorted(sentence.split(),  key=lambda w: pos(w))
  return ' '.join(map(lambda w: no_num(w),  sentence))

