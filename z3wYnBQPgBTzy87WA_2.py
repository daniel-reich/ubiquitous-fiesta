
import numpy as np
​
def rps(s1,s2):
    A = np.array ([ 
    #player1 uses lines    
    #rock paper sciss
                    #  Player2 uses rows        
    [3,   1,    0], #  rock              
    [0,   3,    1], #  paper             
    [1,   0,    3]  #  scissors
    ])
​
    d = {'rock': 0,'paper': 1,'scissors': 2}
    
    result = A[d[s1]][d[s2]]
    if result == 0:
        return "Player 1 wins"
    elif result == 1:
        return "Player 2 wins"
    elif result == 3:
        return "TIE"

