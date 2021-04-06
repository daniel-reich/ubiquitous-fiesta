
import numpy as np
def rps(s1, s2):
    if (s1 == "paper" and s2 ==  "rock") or (s1 == "rock" and s2 == "scissors") or (s1 =="scissors" and s2 =="paper"):
        return "Player 1 wins"
    elif s1 == s2:
        return "TIE"
    else:
        return "Player 2 wins"

