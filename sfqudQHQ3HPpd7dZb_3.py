
def rps(p1, p2):
    d = {'Rock': 1, 'Scissors': 2, 'Paper': 3}
    a = d.get(p1)
    b = d.get(p2)
    dif = a - b
    if dif in [-1, 2]:
        return 'The winner is p1'
    elif dif in [-2, 1]:
        return 'The winner is p2'
    else:
        return "It's a draw"

