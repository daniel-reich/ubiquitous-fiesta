
def roger_shots(lst):
  time, bottles = 0, 6
  for i in lst:
    if i == 'Bang!':
      time += .5; bottles -= 1
    elif i == 'BangBang!':
      time += .5; bottles -= 2
    if not bottles:
      return time

