
def are_true(*args):
  return {
    (0, 0): 'neither',
    (1, 0): 'first',
    (0, 1): 'second',
    (1, 1): 'both'
  }[args]

