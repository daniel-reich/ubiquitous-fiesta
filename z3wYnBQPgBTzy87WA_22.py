
import numpy as np
def rps(s1, s2):
    if s1=='paper' and s2=='rock':
        return "Player 1 wins"
    elif s1=='rock' and s2=='paper':
        return "Player 2 wins"
    elif s1=='scissors' and s2=='paper':
        return "Player 1 wins"
    elif s1=='paper' and s2=='scissors':
        return "Player 2 wins"
    elif s1=='rock' and s2=='scissors':
        return "Player 1 wins"
    elif s1=='scissors' and s1=='rock':
        return "Player 2 wins"
    else:
        return "TIE"

