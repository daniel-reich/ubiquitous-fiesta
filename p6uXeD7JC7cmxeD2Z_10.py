
win = {'R': 'S',
       'P': 'R',
       'S': 'P'}
def calculate_score(lst):
    game = [ 1 if b == win[a] else 0 if a==b else -1 for a, b in lst]
    return 'Abigail' if game.count(1)> game.count(-1) else 'Tie' if game.count(1)== game.count(-1) else 'Benson'

