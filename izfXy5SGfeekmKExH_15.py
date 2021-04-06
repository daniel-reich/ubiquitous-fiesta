
def puzzle_pieces(a1,a2):
    return len(a1) == len(a2) and len(set(list(map(lambda x,y: x + y,a1,a2)))) == 1

