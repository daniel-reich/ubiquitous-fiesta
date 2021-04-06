
def are_true(a, b):
  return {(1,1): 'both', (0,0): 'neither',
      (1,0): 'first', (0,1): 'second'}[a, b]

