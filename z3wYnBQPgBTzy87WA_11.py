
import numpy as np
def rps(s1, s2):
  choices = {"rock":0,"paper":1,"scissors":2}
  result = {0:"TIE",1:"Player 1 wins", 2:"Player 2 wins"}
  arr = np.array([[0,2,1],[1,0,2],[2,1,0]])
  return result[arr[choices[s1]][choices[s2]]]

