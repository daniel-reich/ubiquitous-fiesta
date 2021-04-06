
# ("8888"), ['Lock', 'Arabesque', 'Shimmy', 'Shake'])
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  dance = []
  for x, y in enumerate(str(pin)):
    if not y.isnumeric() or not len(str(pin)) == 4:
      return('Invalid input.')
    if int(x) + int(y) < 10:
      dance += [moves[int(x) + int(y)]]
    else:
      dance += [moves[(int(x) + int(y)) - 10]]
  return(dance)

