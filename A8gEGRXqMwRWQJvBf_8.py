
tic_tac_toe = lambda a: next((x for x in "XO" if [x, x, x] in a or (x, x, x) in zip(*a) or a[0][0] == a[1][1] == a[2][2] == x or a[2][0] == a[1][1] == a[0][2] == x), "Draw")

