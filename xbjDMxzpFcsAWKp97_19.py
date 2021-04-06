
def can_see_stage(seats):
  for i in range(len(seats[0])):
    for j in range(len(seats)-1):
      if seats[j][i] >= seats[j+1][i]:
        return False
  return True

