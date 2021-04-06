
import numpy as np
def rps(s1,s2):
  grid = np.array([['TIE', 'Player 1 wins', 'Player 2 wins'],
          ['Player 2 wins', 'TIE',  'Player 1 wins'],
          ['Player 1 wins', 'Player 2 wins', 'TIE'],])
  d = {'rock': 0, 'paper': 1, 'scissors': 2}
  return grid[d[s2],d[s1]]

