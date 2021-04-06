
def rps(s1, s2):
  rules=[('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]
  if s1==s2: return "TIE"
  elif (s1,s2) in rules: return "Player 1 wins"
  else: return "Player 2 wins"

