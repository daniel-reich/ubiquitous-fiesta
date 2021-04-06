
def tic_tac_toe(inputs):
    winner = {"X":"Player 1 wins","O":"Player 2 wins"}
    columns = list(map(list,zip(*inputs)))
    diag1 = [[inputs[i][i] for i in range(3)]]
    diag2 = [[inputs[::-1][i][i] for i in range(3)]]
    ans = [i for i in columns + diag1 + diag2 + inputs if len(set(i)) == 1]
    return winner[ans[0][0]] if len(ans) == 1 else "It's a Tie"

