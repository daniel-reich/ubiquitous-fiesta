
def possible_path(lst: list) -> bool:
  moves = {1: (2,), 2: (1, 'H'), 'H': (2, 4), 3: (4,), 4: (3, 'H')}
  for i in range(1, len(lst)):
    if lst[i] not in moves[lst[i - 1]]:
      return False
  return True

