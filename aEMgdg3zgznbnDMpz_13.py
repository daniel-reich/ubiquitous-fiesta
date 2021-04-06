
def rotated_words(t):
  rot = lambda w: all(map(lambda x: x in 'HIMNOSWXZ', w))
  return sum(1 for w in set(t.split()) if rot(w))

