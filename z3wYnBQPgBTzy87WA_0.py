
winners = {'rock':'scissors','scissors':'paper','paper':'rock'}
def rps(s1,s2):
  if s1 == s2:
    return 'TIE'
  if winners[s1] == s2:
    return 'Player 1 wins'
  return 'Player 2 wins'

