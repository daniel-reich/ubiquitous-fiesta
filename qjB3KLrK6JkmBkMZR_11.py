
def can_capture(queens):
  pos1 = queens[0]
  pos2 = queens[1]
  if pos1[0] == pos2[0]:
    return True
  elif pos1[1] == pos2[1]:
    return True
  else:
    if abs(ord(pos1[0])-ord(pos2[0])) == abs(int(pos1[1]) - int(pos2[1])):
      return True
    else:
      return False

