
def first_place(road):
  winner = ''.join(road.split('='))
  return winner[-1] if winner else None

