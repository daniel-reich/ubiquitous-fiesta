
def rps(s1, s2):
    wins = [('rock', 'paper'), ('paper', 'scissors'), ('scissors', 'rock')]
    if (s1, s2) in wins:
        return 'Player 2 wins'
    elif (s2, s1) in wins:
        return 'Player 1 wins'
    return 'TIE'

