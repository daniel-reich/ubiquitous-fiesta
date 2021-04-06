
def who_wins_tonight(co, sp, pr, si):
  return 'Tie' if co//pr==sp//si else ['Bill', "Will"][co//pr<sp//si]

