
def tic_tac_toe(inputs):
  s = [list(set(i)) for i in inputs]
  c = [list(set([j[i] for j in inputs])) for i in range(3)]
  if any([i==['X'] for i in s]) or any([i==['X'] for i in c]):
    return 'Player 1 wins'
  if any([i==['O'] for i in s]) or any([i==['O'] for i in c]):
    return 'Player 2 wins'
  if inputs[1][1]=='X':
    if (inputs[0][0]=='X' and inputs[2][2]=='X') or (inputs[0][2]=='X' and inputs[2][0]=='X'):
      return 'Player 1 wins'
  if inputs[1][1]=='O':
    if (inputs[0][0]=='O' and inputs[2][2]=='O') or (inputs[0][2]=='O' and inputs[2][0]=='O'):
      return 'Player 2 wins'
  return "It's a Tie"

