
import numpy as np
def rps(s1, s2):
  a = 'rock'
  b = 'paper'
  c = 'scissors'
  if s1 == a and s2 == b:
    return 'Player 2 wins'
  elif s1 == a and s2== c:
    return 'Player 1 wins'
  elif s1 == a and s2== a:
    return 'TIE'
  elif s1 == b and s2 ==a:
    return 'Player 1 wins'
  elif s1 ==b and s2 ==b:
    return 'TIE'
  elif s1==b and s2 ==c:
    return 'Player 2 wins'
  elif s1 == c and s2 ==a:
    return 'Player 2 wins'
  elif s1== c and s2 ==b:
    return 'Player 1 wins'
  elif s1== c and s2 ==c:
    return 'TIE'

