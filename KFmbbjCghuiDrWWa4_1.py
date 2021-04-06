
def validate_tic_tac_toe(b):
  count = sum('O X'.index(x) - 1 for x in ''.join(b))
​
  if not 0 <= count <= 1:
      return False
​
  b += [''.join(i[k] for i in b) for k in range(3)]
  b += [
      ''.join(b[k][k] for k in range(3)),
      ''.join(b[2 - k][k] for k in range(3))
  ]
​
  return 'XXX' not in b if count < 1 else 'OOO' not in b

