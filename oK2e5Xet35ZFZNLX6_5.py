
def neighboring(txt):
  return all(abs(x-y) == 1 for x,y in zip([ord(c) for c in txt], [ord(c) for c in txt][1:]))

