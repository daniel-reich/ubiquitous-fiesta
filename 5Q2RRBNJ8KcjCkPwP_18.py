
def tic_tac_toe(inputs):
  dic = {'X':1, 'O':2}
  for c in 'XO':
    if [c]*3 in inputs + [list(z) for z in zip(*inputs)] + \
        [[inputs[i][i] for i in range(3)], [inputs[i][2-i] for i in range(3)]]:
        return "Player {} wins".format(dic[c])
  return "It's a Tie"

