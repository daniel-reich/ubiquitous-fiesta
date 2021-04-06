
def calculate_score(games):
  d = {'R': 'S', 'P': 'R', 'S': 'P'}
  s = sum(1 if d[A] == B else 0 if A == B else -1 for A, B in games)
  return 'Abigail' if s > 0 else 'Benson' if s < 0 else 'Tie'

