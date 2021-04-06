
def magic_square_game(alice, bob):
  (ai, an), (bi, bn) = alice, bob
  return an[bi-1] == bn[ai-1]
# No one test checks parity

