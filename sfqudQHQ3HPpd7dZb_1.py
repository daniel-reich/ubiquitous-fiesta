
def rps(p1, p2):
    wins = {('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')}
    if p1 == p2:
        return "It's a draw"
    return 'The winner is {}'.format('p1' if (p1, p2) in wins else 'p2')

