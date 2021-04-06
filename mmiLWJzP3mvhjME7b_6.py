
def divisible(arg, state='S0'):
  if arg == 'state': return state
  if arg == 'stop': return ['accept', 'reject'][state != 'S0']
  if state == 'S0': return func(1) if arg else func(0)
  if state == 'S1': return func(0) if arg else func(2)
  if state == 'S2': return func(2) if arg else func(1)
func = lambda y: lambda x: divisible(x, 'S%s' % y)

