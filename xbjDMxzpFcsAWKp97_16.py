
def can_see_stage(seats):
  for i in range(len(seats)-1):
    for j in range(len(seats[0])):
      if seats[i][j] >= seats[i+1][j]:
        return False
  return True

