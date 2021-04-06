
def neutralise(s1, s2):
  return ''.join('+' if a==b=='+' else '-' if a==b=='-' else '0' for a, b in zip(s1,s2))

