
def tic_tac_toe(inputs):
    d = [''.join(row[i] for i, row in enumerate(inputs)), ''.join(inputs[j][i] for i,j in enumerate(range(2,-1,-1)))]
    r = [''.join(row) for row in inputs] + [''.join(row) for row in list(zip(*inputs))] + d
    return "Player 1 wins" if 'XXX' in r else "Player 2 wins" if 'OOO' in r else "It's a Tie"

