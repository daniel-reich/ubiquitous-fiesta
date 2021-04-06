
def magic_square_game(alice, bob):
  a_score = sum([int(i) for i in alice[1]])
  b_score = sum([int(i) for i in bob[1]])
  if a_score % 2 != 0 and b_score % 2 == 0 and alice[1][bob[0]-1] == bob[1][alice[0]-1]:
    return True
  return False

