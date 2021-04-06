
def magic_square_game(alice, bob):
  a = 0
  for i in alice[1]:
    a += int(i)
  b = 0
  for i in bob[1]:
    b += int(i)
  if a % 2 == 0:
    return False
  if b % 2 != 0:
    return False
  if alice[1][bob[0]-1] != bob[1][alice[0]-1]:
    return False
  return True

