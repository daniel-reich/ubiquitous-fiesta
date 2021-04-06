
def can_capture(queens):
  if (queens[0][0] == queens[1][0] or int(queens[0][1]) == int(queens[1][1])):
    return True
  if (abs(int(queens[0][1]) - int(queens[1][1])) == abs(ord(queens[1][0]) - ord(queens[0][0]))):
    return True
  return False

