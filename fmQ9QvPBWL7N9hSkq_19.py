
def unstretch(word):
  import itertools
​
  return ''.join(c[0] for c in itertools.groupby(word))

