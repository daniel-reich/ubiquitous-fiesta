
def ping_pong(lst, win):
    game = []
    if win == True:
        r = len(lst)*2
    else:
        r = len(lst)*2-1
    for i in range(r):
        if len(game) == 0 or game[-1] == 'Pong!':
            game.append('Ping!')
        else:
            game.append('Pong!')
    return game

