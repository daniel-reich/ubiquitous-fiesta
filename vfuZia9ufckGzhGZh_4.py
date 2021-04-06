
def seq_level(lst):
  def inner(x):
    if len(set(x)) == 1:
      return 0
    return 1 + inner([s - f for f, s in zip(x, x[1:])])
  return ('Linear', 'Quadratic', 'Cubic')[inner(lst) - 1]

