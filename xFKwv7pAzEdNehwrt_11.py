
def bracket_logic(xp):
  a = ''.join([i for i in xp if i in '(){}[]<>'])
  brackets = ['()', '{}', '[]', '<>']
  while any(i in a for i in brackets):
    for i in brackets:
      if i in a: a = a[:a.index(i)] + a[a.index(i)+2:]
  return len(a) == 0

