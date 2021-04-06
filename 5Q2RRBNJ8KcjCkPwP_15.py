
def tic_tac_toe(inputs):
    for row in inputs:
        s = set(row)
        if len(s) == 1:
            res = 1 if s.pop() == 'X' else 2
            return 'Player {} wins'.format(res)
    for col in zip(*inputs):
        s = set(col)
        if len(s) == 1:
            res = 1 if s.pop() == 'X' else 2
            return 'Player {} wins'.format(res)
    d1 = set(inputs[i][i] for i in range(3))
    if len(d1) == 1:
        res = 1 if d1.pop() == 'X' else 2
        return 'Player {} wins'.format(res)
    d2 = set(inputs[i][2 - i] for i in range(3))
    if len(d2) == 1:
        res = 1 if d2.pop() == 'X' else 2
        return 'Player {} wins'.format(res)
    return 'It\'s a Tie'

