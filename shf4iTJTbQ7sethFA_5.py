
def magic_square_game(alice, bob):
  return sum(map(int,alice[1]))%2 and not sum(map(int,bob[1]))%2 and alice[1][bob[0]-1]==bob[1][alice[0]-1]

