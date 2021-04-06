
def possibly_perfect(key, answers):
  return len(set([a == b for a, b in zip(key, answers) if a != '_'])) == 1

