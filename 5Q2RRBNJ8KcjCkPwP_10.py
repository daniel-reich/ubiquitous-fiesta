
from numpy import transpose, diag
def tic_tac_toe(inputs):
  table = inputs
  sym_table = [_[::-1] for _ in table]
  lines = []
  for a in table:
    lines.append(set(a))
  for b in transpose(table):
    lines.append(set(b))
  lines.append(set(diag(table)))
  lines.append(set(diag(sym_table)))
  return 'Player 1 wins' if {'X'} in lines else 'Player 2 wins' if {'O'} in lines else 'It\'s a Tie'

