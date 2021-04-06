
def lengthen(*args):
  s2, s1 = sorted(args, key=len)
  return s2 * (len(s1) // len(s2)) + s2[:len(s1) % len(s2)]

