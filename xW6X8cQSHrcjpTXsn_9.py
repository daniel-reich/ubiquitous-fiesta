
def first_and_last(s):
  x = ''.join(sorted(s))
  return [x, x[::-1]]

