
def will_fit(holds, cargo):
  h = 0
  ca = sum(cargo)
  for i in holds:
    if i == 'S':
      h+=50
    elif i == 'M':
      h+=100
    elif i == 'L':
      h+=200
  if h > ca:
    return True
  else:
    return False

