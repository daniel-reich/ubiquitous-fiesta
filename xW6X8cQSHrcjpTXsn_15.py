
def first_and_last(s):
  first = ''.join(sorted(s))
  last = ''.join(sorted(s, reverse=True))
  return [first, last]

