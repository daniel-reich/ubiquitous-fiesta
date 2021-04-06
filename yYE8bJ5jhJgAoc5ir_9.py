
def bugger(num):
  from numpy import prod
  tick=0
  while num>=10:
    num=prod([int(c) for c in str(num)])
    tick += 1
  return tick

