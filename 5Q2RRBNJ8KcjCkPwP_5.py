
def tic_tac_toe(inputs):
    c = [list(i) for i in zip(*inputs)]
    dlr = [[inputs[0][0], inputs[1][1], inputs[2][2]]]
    drl = [[inputs[2][0], inputs[1][1], inputs[0][2]]]
    for i in inputs + c + dlr + drl:
        if set(i) == {'X'}:
            return 'Player 1 wins'
        elif set(i) == {'O'}:
            return 'Player 2 wins'
    return "It's a Tie"

