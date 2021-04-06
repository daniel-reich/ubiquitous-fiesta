
import numpy as np
​
d = {'rock':0, 'paper':1, 'scissors':2}
def rps(s1, s2):
  if s1==s2: return 'TIE'
  if d[s1] - d[s2] == -1: return "Player 2 wins"
  return "Player 1 wins"

