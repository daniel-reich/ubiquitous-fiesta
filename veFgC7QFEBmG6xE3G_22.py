
def is_smooth(sentence):
  s = sentence.lower().split()
  return all([ x[-1] == y[0] for x, y in zip(s[:-1],s[1:])])

