
def worded_math(equ):
  d = {'zero': 0, 'one': 1, 'two': 2, 'plus': '+', 'minus': '-'}
  res = eval('{}{}{}'.format(*[d[i] for i in equ.lower().split()]))
  return ['Zero', 'One', 'Two'][res]

