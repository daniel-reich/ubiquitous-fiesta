
def worm_length(worm):
  return str(len(worm) * 10) + ' mm.' if all([i == '-' for i in worm]) and worm else 'invalid'

