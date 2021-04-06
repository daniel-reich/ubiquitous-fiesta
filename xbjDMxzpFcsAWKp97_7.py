
def can_see_stage(seats):
  for col in range(len(seats[0])):
    if not all([seats[row][col] < seats[row + 1][col] for row in range(len(seats) - 1)]):
      return False
    
  return True

