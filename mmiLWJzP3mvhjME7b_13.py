
def divisible(arg, S=0):
  if arg == 'state': return 'S{}'.format(S)
  if arg == 'stop': return ('reject', 'accept')[not S]
  return lambda x: divisible(x, {0: [0, 1], 1: [2, 0], 2: [1, 2]}[S][arg])

