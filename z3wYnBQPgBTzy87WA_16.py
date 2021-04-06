
def rps(s1, s2):
  win={"rock":"paper","paper":"scissors","scissors":"rock"}
  return "TIE" if s1==s2 else "Player 2 wins" if win[s1]==s2 else "Player 1 wins"

