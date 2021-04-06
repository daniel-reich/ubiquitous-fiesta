
def can_capture(queens):
  frstpos="ABCDEFGH"
  if queens[0][0]==queens[1][0] or queens[0][1]==queens[1][1]:
    return True
  elif queens[1][0] in frstpos and queens[1][1]==str(frstpos.index(queens[1][0])-frstpos.index(queens[0][0])+int(queens[0][1])):
      return True
  elif queens[1][0] in frstpos and queens[1][1]==str(frstpos.index(queens[0][0])-frstpos.index(queens[1][0])+int(queens[0][1])):
      return True
  return False

