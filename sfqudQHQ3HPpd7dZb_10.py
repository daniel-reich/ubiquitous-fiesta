
def rps(p1, p2):
    retstr = 'The winner is '
    if p1 == p2:
        return 'It\'s a draw'
    elif p1 == 'Rock' and p2 == 'Scissors':
        return retstr+'p1'
    elif p1 == 'Paper' and p2 == 'Rock':
        return retstr+'p1'
    elif p1 == 'Scissors' and p2 == 'Paper':
        return retstr+'p1'
    elif p2 == 'Rock' and p1 == 'Scissors':
        return retstr+'p2'
    elif p2 == 'Paper' and p1 == 'Rock':
        return retstr+'p2'
    elif p2 == 'Scissors' and p1 == 'Paper':
        return retstr+'p2'
    # this is pretty clunky, prone to misspellings (for me)
    # looking forward to seeing other solutions

