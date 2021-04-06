
def divisible(arg):
  return aut(0)(arg)
​
def aut(state):
  def meh(arg):
    if arg == 'state':
      return 'S{}'.format(state)
    if arg == 'stop':
      return 'reject' if state else 'accept'
    if state == 0:
      return aut(arg)
    if state == 1:
      return aut(0 if arg ==1 else 2)
    if state == 2:
      return aut(state - 1 + arg)
  return meh

