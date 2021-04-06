
def lengthen(s1, s2):
  return (s2 * len(s1))[:len(s1)] if len(s1) > len(s2) else lengthen(s2, s1)

