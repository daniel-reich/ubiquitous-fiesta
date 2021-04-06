
def anagram(name, words):
  a = sorted([x for x in (''.join(words)).lower()])
  b = sorted([x for x in name.lower() if x!=' '])
  return a==b

