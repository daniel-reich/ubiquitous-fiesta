
def will_fit(holds, cargo):
  space = 0
  for item in holds:
    if item == 'M':
      space += 100
    elif item == 'L':
      space += 200
    elif item == 'S':
      space += 50
  return True if sum(cargo) < space else False

