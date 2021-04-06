
def rps(p1, p2):
  myDict = {
    'Rock': 2,
    'Scissors': 1,
    'Paper': 0
  }
  result = myDict[p1] - myDict[p2]
  if result == 1 or result == -2:
    return 'The winner is p1'
  elif result == -1 or result == 2:
    return 'The winner is p2'
  elif result == 0:
    return "It's a draw"

