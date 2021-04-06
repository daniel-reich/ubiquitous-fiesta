
'''
Rock beats scissors, paper beats rock, scissors beat paper
"Player 1 wins"
"Player 2 wins"
"TIE" (if both inputs are the same)
'''
import numpy as np
def rps(s1, s2):
  if s1 == "rock" and s2 == "scissors":
    return "Player 1 wins"
    
  elif s2 == "rock" and s1 == "scissors":
    return "Player 2 wins"
    
  elif s1 == "paper" and s2 == "rock":
    return "Player 1 wins"
    
  elif s2 == "paper" and s1 == "rock":
    return "Player 2 wins"
    
  elif s1 == "scissors" and s2 == "paper":
    return "Player 1 wins"
    
  elif s2 == "scissors" and s1 == "paper":
    return "Player 2 wins"
    
  elif s1 == s2: 
    return 'TIE'

