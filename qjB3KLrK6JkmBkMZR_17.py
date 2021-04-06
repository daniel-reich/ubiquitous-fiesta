
def can_capture(queens):
  if queens[0][0] == queens[1][0] or queens[0][1] == queens[1][1]:
    return True
  else:
    ax = ord(queens[0][0])
    ay = ord(queens[0][1])
    ox = ord(queens[1][0])
    oy = ord(queens[1][1])
    if abs(ax-ox) == abs(ay-oy):
      return True
    else:
      return False

