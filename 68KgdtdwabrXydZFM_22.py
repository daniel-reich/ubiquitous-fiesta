
def generation(x, y):
  g = {-3: ['great grandfather', 'great grandmother'],
      -2: ['grandfather', 'grandmother'],
      -1: ['father', 'mother'], 
      0: ['me!', 'me!'],
      1: ['son', 'daughter'],
      2: ['grandson', 'granddaughter'],
      3: ['great grandson', 'great granddaughter']}
  return g[x][y=='f']

