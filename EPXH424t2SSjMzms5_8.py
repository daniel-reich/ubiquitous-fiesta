
def remix(txt, lst):
  x = sorted(list(zip(list(txt), lst)), key = lambda x: x[1])
  return ''.join([x[i][0] for i in range(len(x))])

