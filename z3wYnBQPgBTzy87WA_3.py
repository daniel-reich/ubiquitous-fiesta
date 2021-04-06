
def rps(s1, s2):
    outcomes = {('rock', 'scissors'): 'Player 1 wins', 
                ('rock', 'paper'): 'Player 2 wins', 
                ('paper', 'rock'): 'Player 1 wins', 
                ('paper', 'scissors'): 'Player 2 wins', 
                ('scissors', 'paper'): 'Player 1 wins', 
                ('scissors', 'rock'): 'Player 2 wins'}
    return outcomes.get((s1, s2), 'TIE')

