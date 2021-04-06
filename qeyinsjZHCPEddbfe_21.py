
dice_game = lambda r: 0 if any(x==y for (x, y) in r) else sum(x+y for (x, y) in r)

