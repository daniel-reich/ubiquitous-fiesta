
def grant_the_hint(txt):
  words = txt.split()
  strings = []
  for i in range(max([len(word) for word in words]) + 1):
    strings.append(' '.join([word[:i] + '_'*max(0, len(word)-i) for word in words]))
  return strings

