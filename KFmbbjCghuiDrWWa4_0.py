
wins = [{(0, 0), (0, 1), (0, 2)}, {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)}, {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)}, {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)}, {(2, 0), (1, 1), (0, 2)}]
def validate_tic_tac_toe(board):
    cross = set()
    nulls = set()
    for r, row in enumerate(board):
        for c, v in enumerate(row):
            if v == "X":
                cross.add((r, c))
            elif v == "O":
                nulls.add((r, c))
    n_cross = len(cross)
    n_nulls = len(nulls)
    cross_wins = sum(s <= cross for s in wins)
    nulls_wins = sum(s <= nulls for s in wins)
    return ((cross_wins in (1, 2) and nulls_wins == 0
             and n_cross == n_nulls + 1)
            or (nulls_wins in (1, 2) and cross_wins == 0
                and n_cross == n_nulls)
            or (cross_wins == 0 and nulls_wins == 0 and
                n_cross in (n_nulls, n_nulls + 1)))

