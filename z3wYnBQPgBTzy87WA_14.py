
def rps(s1, s2):
  if s1 == s2:
    return "TIE"
  elif s1 == "rock" and s2 == "scissors":
    return "Player 1 wins"
  elif s1 == "paper" and s2 == "rock":
    return "Player 1 wins"
  elif s1 == "scissors" and s2 == "paper":
    return "Player 1 wins"
  else:
    return "Player 2 wins"

