
def tic_tac_toe(inputs):
  row = [i for i in inputs]
  col = [[inputs[i][j] for i in range(3)] for j in range(3)]
  dia = [[inputs[i][i] for i in range(len(inputs))], [inputs[i][len(inputs)-1-i] for i in range(len(inputs))]]
  a = [i[0] for i in row + col + dia if len(set(i))==1]
  return "Player {} wins".format([1,2][a[0]!="X"]) if a!=[] else "It's a Tie"

