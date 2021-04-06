
def generation(x, y):
  g = {-3: {'m': 'great grandfather', 'f': 'great grandmother'},
       -2: {'m': 'grandfather', 'f': 'grandmother'},
     -1: {'m': 'father', 'f': 'mother'},
      0: {'m': 'me!', 'f': 'me!'},
      1: {'m': 'son', 'f': 'daughter'},
      2: {'m': 'grandson', 'f': 'granddaughter'},
      3: {'m': 'great grandson', 'f': 'great granddaughter'}}
  if x == 0:
    return 'me!'
  else:
    return g[x][y]

