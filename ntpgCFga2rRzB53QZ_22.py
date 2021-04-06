
def staircase(n):
  if n == 1:
    return "#"
  pos_n = n if n > 0 else -n
  previous = staircase(pos_n - 1)
  lines = []
  for st in previous.splitlines():
    lines.append('_' + st)
  lines.append(pos_n * '#')
  return '\n'.join(lines) if n > 0 else '\n'.join(lines[::-1])

