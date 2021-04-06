
def can_capture(queens):
  if queens[0][0]==queens[1][0] or queens[0][1]==queens[1][1]:
    return True
  elif abs(ord(queens[0][0])-ord(queens[1][0]))==\
  abs(int(queens[0][1])-int(queens[1][1])):
    return True
  else:
    return False

