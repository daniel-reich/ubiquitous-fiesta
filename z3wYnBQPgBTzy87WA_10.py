
def rps(s1, s2):
  rps = ['paper','scissors', 'rock']
  s1,s2 = rps.index(s1),rps.index(s2)
  s = s1-s2
  s = -1 if s == 2 else 1 if s == -2 else s
  return "Player 1 wins" if s > 0 else "Player 2 wins" if s < 0 else "TIE"

