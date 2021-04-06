
def first_and_last(s):
  s = ''.join(sorted(s))
  return [s, s[::-1]]

