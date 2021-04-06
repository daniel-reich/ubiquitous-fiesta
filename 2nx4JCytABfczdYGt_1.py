
def conjugate(verb, pronoun):
  d = {1: ('Io', 'o'), 2: ('Tu', 'i'), 3: ('Egli', 'a'), 4: ('Noi', 'iamo'),
      5: ('Voi', 'ate'), 6: ('Essi', 'ano')}
  root = verb[:-3].lower()
  if root[-1] in 'cg' and pronoun in (2, 4): root = root + 'h'
  if root[-1] == 'i' and pronoun in (2, 4): root = root[:-1]
  return d[pronoun][0] + ' ' + root + d[pronoun][1]

