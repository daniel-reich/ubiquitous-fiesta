
import numpy as np
def rps(s1, s2):
  if s1 == s2:
    return "TIE"
  elif s1 == "rock" and s2 =="paper" or s1 == "paper" and s2 == "scissors":
    return "Player 2 wins"
  else:
    return "Player 1 wins"

