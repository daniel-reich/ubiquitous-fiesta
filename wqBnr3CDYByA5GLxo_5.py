
def unravel(txt):
  unravelled = []
  remaining = [(txt, '')]
  while len(remaining) != 0:
    nextrem = remaining.pop(0)
    start = nextrem[0].find('[')
    if start != -1:
      close = nextrem[0].find(']')
      options = nextrem[0][start+1:close].split('|')
      for o in options:
        remaining.append((nextrem[0][close+1:], \
                          nextrem[1]+nextrem[0][:start]+o))
    else:
        unravelled.append(nextrem[1]+nextrem[0])
  return sorted(unravelled)

