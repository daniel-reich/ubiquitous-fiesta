
def rps(p1, p2):
    
    if p1 == p2:
        return "It's a draw"
    
    elif p1 == "Rock":
        if p2 == "Paper":
            winner = "p2"
        else:
            winner = "p1"
​
    elif p1 == "Paper":
        if p2 == "Scissors":
            winner = "p2"
        else:
            winner = "p1"    
​
    elif p1 == "Scissors":
        if p2 == "Rock":
            winner = "p2"
        else:
            winner = "p1"
    
    return "The winner is " + winner

