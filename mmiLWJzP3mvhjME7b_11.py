
def divisible(arg, state = 0):
  states = [{0: 0, 1: 1},
            {0: 2, 1: 0},
            {0: 1, 1: 2}]
  if arg == 'state':
    return 'S' + str(state)
  elif arg == 'stop':
    return 'accept' if state == 0 else 'reject'
  else:
    return lambda x: divisible(x, state = states[state][arg])

