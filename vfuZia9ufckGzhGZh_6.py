
def seq_level(lst, c=0):
  diff = [b - a for a, b in zip(lst, lst[1:])]
  if len(set(diff)) == 1:
    return ['Linear', 'Quadratic', 'Cubic'][c]
  c += 1
  return seq_level(diff, c)

