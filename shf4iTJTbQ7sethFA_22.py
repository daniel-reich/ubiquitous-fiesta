
def magic_square_game(alice, bob):
    return alice[1][bob[0]-1] == bob[1][alice[0]-1]

