
def divisible(arg, state='S0'):
  machine = { 'S0': ('S0', 'S1'), 'S1': ('S2', 'S0'), 'S2': ('S1', 'S2') }
  accept_state = 'S0'
  def transition(b):
    return divisible(b, machine[state][arg])
  if arg in [0, 1]:
    return transition
  rtn = None
  if arg == 'state':
    rtn = state
  if arg == 'stop':
    rtn = 'accept' if state == accept_state else 'reject'
  return rtn

