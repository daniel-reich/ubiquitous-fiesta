
def hats(lst):
  reqd, lines = lst
  start = int(reqd / sum(1 / line for line in lines))
  stop = start + min(lines) + 1
  for t in range(start, stop):
    num = sum(t // line for line in lines)
    if num == reqd:
      pl = 's' if t > 1 else ''
      return '{} minute{}'.format(t, pl)
  return None

