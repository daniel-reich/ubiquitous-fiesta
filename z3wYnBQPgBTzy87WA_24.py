
import numpy as np
def rps(s1, s2):
  if s1 == s2:
    return 'TIE'
  elif s1 == 'paper':
    if s2 == 'scissors':
      return 'Player 2 wins'
    else:
      return 'Player 1 wins'
  elif s1 == 'scissors':
    if s2 == 'paper':
      return 'Player 1 wins'
    else:
      return 'Player 2 wins'
  elif s1 == 'rock':
    if s2 == 'paper':
      return 'Player 2 wins'
    else:
      return 'Player 1 wins'

