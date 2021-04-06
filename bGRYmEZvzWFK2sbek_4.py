
alphaset = set(chr(a) for a in range(97, 123))
def get_missing_letters(s):
  return ''.join(sorted(alphaset - set(s)))

