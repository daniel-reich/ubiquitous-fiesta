
def divisible(val):
  state = 'S0'
  if val == 'state':
      return state
  if val == 'stop':
      return 'accept'
​
  if val == 1:
      state = 'S1'
​
  def inner(val):
      nonlocal state
​
      if val == 'state':
          return state
      if val == 'stop':
          if state == 'S0':
              return 'accept'
          else:
              return 'reject'
​
      if state == 'S0' and val == 1:
          state = 'S1'
      elif state == 'S1':
          if val == 0:
              state = 'S2'
          else:
              state = 'S0'
      elif state == 'S2' and val == 0:
          state = 'S1'
​
      return inner
​
  return inner

