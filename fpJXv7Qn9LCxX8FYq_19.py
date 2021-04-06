
def solve(eq):
  tail = list(map(int, eq[3:].split(' = ')))
  if eq[2] == '+':
    return tail[1] - tail[0]
  return tail[0] + tail[1]

