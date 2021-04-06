
def percent_filled(box):
  spaces, balls = 0, 0
  for i in box:
    spaces += i.count(' ')
    balls += i.count('o')
  return '{}%'.format(round(balls / (spaces + balls) * 100))

