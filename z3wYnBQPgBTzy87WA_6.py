
def rps(s1,s2):
    if s1 == s2: return "TIE"
    if s1[0] == "r":
      return 'Player 2 wins' if s2[0] == "p" else 'Player 1 wins'
    if s1[0] == "p":
      return 'Player 2 wins' if s2[0] == "s" else 'Player 1 wins'
      if s2[0] == "r": return 'Player 1 wins'
    if s1[0] == "s":
      return 'Player 2 wins' if s2[0] == "r" else 'Player 1 wins'

